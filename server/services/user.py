import bcrypt
from fastapi import Depends, HTTPException, status
from typing import Annotated

from models import User
from schemas import UserAuthSchema, UserSchema
from repositories import UserRepositoryDependency
from utils.access_token import create_access_token, verify_access_token

class UserService:
    def __init__(self, user_repository: UserRepositoryDependency): 
        self.repository = user_repository

    def create_user(self, user: UserAuthSchema) -> str:
        hashed_password = bcrypt.hashpw(
            user.password.encode('utf-8'), bcrypt.gensalt()
        ).decode("utf-8")
        user.password = hashed_password
        new_user = self.repository.create_user(user)

        token_data = {
            "id" : new_user.id,
            "email" : new_user.email
        }

        access_token = create_access_token(token_data)
        return access_token
    
    def login_user(self, user_auth: UserAuthSchema) -> str:
        user = self.repository.get_user_by_email(user_auth.email)
        password_check = bcrypt.checkpw(
            user_auth.password.encode("utf-8"), user.password.encode("utf-8")
        )

        if user is None or not password_check:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
        
        token_data = {
            "id" : user.id,
            "email" : user.email
        }

        access_token = create_access_token(token_data)
        return access_token

    def update_token (self, token: str | None) -> str:
        decoded = verify_access_token(token)
        new_access_token = create_access_token(decoded)
        return new_access_token
            

    def get_user(self, id: int | None, email: str | None) -> UserSchema:
        user = None

        if id:
            user = self.repository.get_user_by_id(id)
        elif email is not None:
            user = self.repository.get_user_by_email(email)
        else: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Some of args are missing")
        
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user was not found")
        print(user)
        return UserSchema.model_validate(user)
    
    def delete_user(self, id: int) -> str:
        user = self.repository.get_user_by_id(id)

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user was not found")
        
        self.repository.delete_user(user)
        return "User was deleted"

UserServiceDependency = Annotated[UserService, Depends(UserService)]
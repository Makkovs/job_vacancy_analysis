import bcrypt
from fastapi import Depends
from typing import Annotated

from schemas import UserAuthSchema, UserSchema
from repositories import UserRepositoryDependency
from utils.access_token import create_access_token, verify_access_token
from exception import UserNotFoundError, AccessDeniedError, UnauthorizedError

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

        return create_access_token(token_data)
    
    def login_user(self, user_auth: UserAuthSchema) -> str:
        user = self.repository.get_user_by_email(user_auth.email)
        
        if user is None:
            raise UnauthorizedError(message="Invalid email or password!")

        password_check = bcrypt.checkpw(
            user_auth.password.encode("utf-8"), user.password.encode("utf-8")
        )

        if not password_check:
            raise UnauthorizedError(message="Invalid email or password!")
        
        token_data = {
            "id" : user.id,
            "email" : user.email
        }

        access_token = create_access_token(token_data)
        return access_token

    def update_token (self, token: str | None) -> str:
        decoded = verify_access_token(token)
        new_token = {
            "id" : decoded["id"],
            "email" : decoded["email"]
        }
         
        return create_access_token(new_token)
            
    def get_user(self, id: int) -> UserSchema:
        user = self.repository.get_user_by_id(id)        
        if user is None:
            raise UserNotFoundError(id)
        return UserSchema.model_validate(user)
    
    def delete_user(self, id: int, token: str) -> str:
        decoded = verify_access_token(token)
        if decoded["id"] != id:
            raise AccessDeniedError()
    
        user = self.repository.get_user_by_id(id)
        if user is None:
            raise UserNotFoundError(id)
        
        self.repository.delete_user(user)
        return "User was deleted"

UserServiceDependency = Annotated[UserService, Depends(UserService)]
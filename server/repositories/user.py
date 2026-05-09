from typing import Annotated
from fastapi import Depends
from sqlalchemy import select

from models import User
from repositories import BaseRepository
from schemas import UserAuthSchema

class UserRepository(BaseRepository):

    def create_user(self, user: UserAuthSchema) -> User:
        new_user = User(email = user.email, password = user.password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        return new_user
    
    def get_user_by_email(self, email: str) -> User:
        query = select(User).where(User.email == email)
        return self.db.execute(query).scalar_one_or_none()
    
    def get_user_by_id(self, id: int) -> User:
        query = select(User).where(User.id == id)
        return self.db.execute(query).scalar_one_or_none()

    def delete_user(self, user: User) -> bool:
        self.db.delete(user)
        self.db.commit()

UserRepositoryDependency = Annotated[UserRepository, Depends(UserRepository)]
from fastapi import Depends
from typing import Annotated
from sqlalchemy import select

from models import User
from schemas import UserAuthSchema
from repositories import BaseRepository

class UserRepository(BaseRepository):

    async def create_user(self, user: UserAuthSchema) -> User:
        new_user = User(email = user.email, password = user.password)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        
        return new_user
    
    async def get_user_by_email(self, email: str) -> User:
        query = select(User).where(User.email == email)
        return await self.db.scalar(query)
    
    async def get_user_by_id(self, id: int) -> User:
        query = select(User).where(User.id == id)
        return await self.db.scalar(query)

    async def delete_user(self, user: User) -> bool:
        await self.db.delete(user)
        await self.db.commit()

UserRepositoryDependency = Annotated[UserRepository, Depends(UserRepository)]
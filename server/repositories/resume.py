from fastapi import Depends
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models import Resume, ResumeSkill
from repositories import BaseRepository
from exception import ResumeNotFoundError
from schemas import ResumeSchemaCreate, ResumeSchemaUpdate

class ResumeRepository(BaseRepository):

    async def create_resume(self, resume: ResumeSchemaCreate, user_id: int):
        new_resume = Resume(
            title=resume.title,
            description = resume.description, 
            user_id = user_id, 
            skill_ids=resume.skill_ids
        )
        
        self.db.add(new_resume)
        await self.db.commit()

        query = (
            select(Resume)
            .where(Resume.id == new_resume.id)
            .options(selectinload(Resume.resume_skills).selectinload(ResumeSkill.skill))
        )

        return await self.db.scalar(query)

    async def get_resumes(self, user_id: int): 
        query = (
            select(Resume)
            .where(Resume.user_id == user_id)
            .options(selectinload(Resume.resume_skills).selectinload(ResumeSkill.skill))
        )
        return await self.db.scalars(query)

    async def get_resume_by_id(self, resume_id: int, user_id: int):
        query = (
            select(Resume)
            .where(Resume.id == resume_id, Resume.user_id == user_id)
            .options(selectinload(Resume.resume_skills).selectinload(ResumeSkill.skill))
        )
        return await self.db.scalar(query)

    async def delete_resume(self, resume: Resume):
        await self.db.delete(resume)
        await self.db.commit()

    async def patch_resume(self, resume_id: int, user_id: int, resume_dto: ResumeSchemaUpdate):
        query = (
            select(Resume)
            .where(Resume.id == resume_id, Resume.user_id == user_id)
            .options(selectinload(Resume.resume_skills).selectinload(ResumeSkill.skill))    
        )
        resume = await self.db.scalar(query)

        if not resume:
            raise ResumeNotFoundError(resume_id)

        update_data = resume_dto.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(resume, field, value)

        await self.db.commit()
        await self.db.refresh(resume)

        return resume

ResumeRepositoryDependency = Annotated[ResumeRepository, Depends(ResumeRepository)]
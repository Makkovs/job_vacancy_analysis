from fastapi import Depends
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models import Resume, ResumeSkill
from repositories import BaseRepository
from exception import ResumeNotFoundError
from schemas import ResumeSchemaCreate, ResumeSchemaUpdate

class ResumeRepository(BaseRepository):

    def create_resume(self, resume: ResumeSchemaCreate, user_id: int):
        new_resume = Resume(title=resume.title, description = resume.description, user_id = user_id, skill_ids=resume.skill_ids)
        self.db.add(new_resume)
        self.db.commit()
        self.db.refresh(new_resume, attribute_names=["resume_skills"])

        return new_resume

    def get_resumes(self, user_id: int): 
        query = select(Resume).where(Resume.user_id == user_id)
        return self.db.execute(query).scalars().all()

    def get_resume_by_id(self, resume_id: int, user_id: int):
        query = select(Resume).where(Resume.id == resume_id,  Resume.user_id == user_id)
        return self.db.execute(query).scalar_one_or_none()

    def delete_resume(self, resume_id: int, user_id: int):
        query = select(Resume).where(Resume.id == resume_id, Resume.user_id == user_id)
        resume = self.db.scalar(query)

        if not resume:
            raise ResumeNotFoundError(resume_id)

        self.db.delete(resume)
        self.db.commit()

    def patch_resume(self, resume_id: int, user_id: int, resume_dto: ResumeSchemaUpdate):
        query = (
            select(Resume)
            .where(Resume.id == resume_id, Resume.user_id == user_id)
            .options(selectinload(Resume.resume_skills).selectinload(ResumeSkill.skill))    
        )
        resume = self.db.scalar(query)

        if not resume:
            raise ResumeNotFoundError(resume_id)

        update_data = resume_dto.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(resume, field, value)

        self.db.commit()
        self.db.refresh(resume)

        return resume

ResumeRepositoryDependency = Annotated[ResumeRepository, Depends(ResumeRepository)]
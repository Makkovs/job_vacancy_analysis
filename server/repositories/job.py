from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from typing import Annotated
from fastapi import Depends

from models import Job, Skill, JobSkill
from schemas import JobFilters
from repositories import BaseRepository

class JobRepository(BaseRepository):

    def get_jobs(self, filters: JobFilters):
        query = select(Job).options(selectinload(Job.job_skills))   
        if filters.skill_ids is not None:
            query = query.where(Job.job_skills.any(JobSkill.skill_id.in_(filters.skill_ids)))

        if filters.salary_min is not None:
            query = query.where(Job.salary_max >= filters.salary_min)

        if filters.salary_max is not None:
            query = query.where(Job.salary_max <= filters.salary_max)

        if filters.country is not None:
            query = query.where(func.lower(Job.country) == func.lower(filters.country))
  
        if filters.qualification is not None:
            query = query.where(Job.qualification >= filters.qualification)

        if filters.experience is not None:
            query = query.where(Job.experience <= filters.experience)

        offset = (filters.page - 1) * filters.page_size
        query = query.offset(offset).limit(filters.page_size)

        return self.db.execute(query).scalars().all()

    def get_job_by_id(self, id: int): 
        query = select(Job).where(Job.id == id)
        return self.db.execute(query).scalar_one_or_none()

JobRepositoryDependency = Annotated[JobRepository, Depends(JobRepository)]
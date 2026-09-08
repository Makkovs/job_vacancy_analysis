from fastapi import Depends
from typing import Annotated
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from schemas import JobFilters
from models import Job, JobSkill
from repositories import BaseRepository

class JobRepository(BaseRepository):

    async def get_jobs(self, filters: JobFilters):
        query = select(Job).options(
            selectinload(Job.job_skills).joinedload(JobSkill.skill)
        )
        if filters.skill_ids is not None:
            query = (
                query
                .join(Job.job_skills)
                .where(JobSkill.skill_id.in_(filters.skill_ids))
                .group_by(Job.id)
                .having(func.count(func.distinct(JobSkill.skill_id)) == len(filters.skill_ids))
            )
            
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

        return (await self.db.scalars(query)).all()

    async def get_job_by_id(self, job_id: int): 
        query = (
            select(Job)
            .where(Job.id == job_id)
            .options(
                selectinload(Job.job_skills).joinedload(JobSkill.skill))
        )  
        return await self.db.scalar(query)

JobRepositoryDependency = Annotated[JobRepository, Depends(JobRepository)]
from sqlalchemy import select, case
from sqlalchemy.orm import selectinload
from typing import Annotated
from fastapi import Depends

from models import Job, Skill, JobSkill
from schemas import JobFilters
from repositories import BaseRepository

class JobRepository(BaseRepository):

    def get_jobs(self, filters: JobFilters):
        query = select(Job).options(selectinload(Job.job_skills).selectinload(JobSkill.skill))

        if filters.skill_ids is not None:
            query = query.where(Job.job_skills.any(Skill.id.in_(filters.skill_ids)))

        if filters.salary_min is not None:
            query = query.where(Job.salary_max >= filters.salary_min)

        if filters.salary_max is not None:
            query = query.where(Job.salary_max <= filters.salary_max)

        if filters.country is not None:
            query = query.where(Job.country == filters.country)

        if filters.qualification is not None:
            query = query.where(Job.qualification >= filters.qualification)

        if filters.experience is not None:
            query = query.where(Job.experience <= filters.experience)

        return self.db.execute(query).scalars().all()

JobRepositoryDependency = Annotated[JobRepository, Depends(JobRepository)]
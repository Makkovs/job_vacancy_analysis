from sqlalchemy import select
from typing import Annotated
from fastapi import Depends

from models import Job, Skill
from schemas import JobFilters
from repositories import BaseRepository
from utils.qualification_map import QUALIFICATION_REVERSE_MAP

class JobRepository(BaseRepository):
    
    def get_jobs(self, filters: JobFilters):
        query = select(Job)

        if filters.skill_ids is not None:
            query = query.where(Job.job_skills.any(Skill.id.in_(filters.skill_ids)))

        if filters.salary_min is not None:
            query = query.where(Job.salary_max >= filters.salary_min)

        if filters.salary_max is not None:
            query = query.where(Job.salary_max <= filters.salary_max)

        if filters.country is not None:
            query = query.where(Job.country == filters.country)

        if filters.qualification is not None:
            query = query.where(QUALIFICATION_REVERSE_MAP[Job.qualification] >= filters.qualification(Job.qualification))

        if filters.experience is not None:
            query = query.where(Job.experience <= filters.experience)

        return self.db.execute(query).all()

JobRepositoryDependency = Annotated[JobRepository, Depends(JobRepository)]
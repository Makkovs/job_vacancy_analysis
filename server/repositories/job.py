from fastapi import Depends
from typing import Annotated
from sqlalchemy import select, func, and_, desc
from sqlalchemy.orm import selectinload

from schemas import JobFilters
from models import Job, JobSkill, Skill
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
            query = query.where(Job.country.ilike(f"%{filters.country}%"))
  
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

    async def get_stats(self, filters: JobFilters):
        conditions = []
                    
        if filters.salary_min is not None:
            conditions.append(Job.salary_max >= filters.salary_min)

        if filters.salary_max is not None:
            conditions.append(Job.salary_max <= filters.salary_max)

        if filters.country is not None:
            conditions.append(Job.country.ilike(f"%{filters.country}%"))
    
        if filters.qualification is not None:
            conditions.append(Job.qualification >= filters.qualification)

        if filters.experience is not None:
            conditions.append(Job.experience <= filters.experience)

        if filters.skill_ids is not None:
            conditions.append(JobSkill.skill_id.in_(filters.skill_ids))


        stats_query = (
            select(
                func.count(func.distinct(Job.id)).label("total_jobs"),
                func.min(Job.salary_min).label("salary_min"),
                func.max(Job.salary_max).label("salary_max"),
                func.round(func.avg(Job.salary_max)).label("salary_avg"),
                func.percentile_cont(0.25)
                    .within_group(Job.salary_max).label("salary_p25"),
                func.percentile_cont(0.50)
                    .within_group(Job.salary_max).label("salary_median"),
                func.percentile_cont(0.75)
                    .within_group(Job.salary_max).label("salary_p75")
            )
        )

        if filters.skill_ids:
            stats_query = stats_query.join(Job.job_skills)

        if conditions:
            stats_query = stats_query.where(and_(*conditions))

        stats_res = (await self.db.execute(stats_query)).one()

        if not stats_res.total_jobs:
            return {
                "total_jobs" : 0, 
                "salary_min" : 0, "salary_max" : 0, "salary_avg" : 0,
                "salary_median" : 0, "salary_p25" : 0, "salary_p75" : 0,
                "top_skills" : []
            }

        top_skills_query = (
            select (
                Skill.id,
                Skill.name,
                func.count(JobSkill.job_id).label("frequency")
            )
            .join(JobSkill, Skill.id == JobSkill.skill_id)
            .join(Job, Job.id == JobSkill.job_id)
        )

        if conditions:
            top_skills_query = top_skills_query.where(and_(*conditions))

        if filters.skill_ids:
            top_skills_query = top_skills_query.where(Skill.id.not_in(filters.skill_ids))

        top_skills_query = (
            top_skills_query
            .group_by(Skill.id, Skill.name)
            .order_by(desc("frequency"))
            .limit(7)
        )

        top_skills_query = (await self.db.execute(top_skills_query)).all()

        return {
            "total_jobs" : stats_res.total_jobs,
            "salary_min" : int(stats_res.salary_min),
            "salary_max" : int(stats_res.salary_max),
            "salary_avg" : int(stats_res.salary_avg),
            "salary_median" : int(stats_res.salary_median),
            "salary_p25" : int(stats_res.salary_p25),
            "salary_p75" : int(stats_res.salary_p75),
            "top_skills" : top_skills_query
        }

        

JobRepositoryDependency = Annotated[JobRepository, Depends(JobRepository)]
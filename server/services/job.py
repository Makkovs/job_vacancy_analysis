from fastapi import Depends
from typing import Annotated, List

from models import Job
from schemas import JobFilters, JobStatsSchema
from repositories import JobRepositoryDependency

class JobService: 
    
    def __init__(self, job_repository: JobRepositoryDependency):
        self.repository = job_repository

    async def get_jobs(self, filters: JobFilters) -> List[Job]:
        return await self.repository.get_jobs(filters)

    async def get_job_by_id(self, job_id: int) -> Job:
        return await self.repository.get_job_by_id(job_id)

    async def get_stats(self, filters: JobFilters) -> JobStatsSchema:
        return await self.repository.get_stats(filters)

JobServiceDependency = Annotated[JobService, Depends(JobService)]
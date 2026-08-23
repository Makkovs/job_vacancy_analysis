from fastapi import Depends
from typing import Annotated, List

from models import Job
from repositories import JobRepositoryDependency
from schemas import JobFilters, JobSchema

class JobService: 
    
    def __init__(self, job_repository: JobRepositoryDependency):
        self.repository = job_repository

    def get_jobs(self, filters: JobFilters) -> List[Job]:
        jobs = self.repository.get_jobs(filters)
        return jobs

JobServiceDependency = Annotated[JobService, Depends(JobService)]
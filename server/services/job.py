from fastapi import Depends
from typing import Annotated

from schemas import JobFilters

class JobService: 
    
    def __init__(self):
        pass

    def get_jobs(filters: JobFilters):
        pass

JobServiceDependency = Annotated[JobService, Depends(JobService)]
from fastapi import APIRouter, Depends, Query
from typing import Annotated, List
from schemas import JobFilters, JobSchema
from services import JobServiceDependency

job_router = APIRouter(prefix="/job", tags=["job"])

@job_router.get("/", response_model=List[JobSchema])
def get_jobs(
    filters: Annotated[JobFilters, Query()],
    service: JobServiceDependency = JobServiceDependency
):
    return service.get_jobs(filters)
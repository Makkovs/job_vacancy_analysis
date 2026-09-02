from fastapi import APIRouter, Query
from typing import Annotated, List
from schemas import JobFilters, JobGetSchema
from services import JobServiceDependency

job_router = APIRouter(prefix="/job", tags=["job"])

@job_router.get("/", response_model=List[JobGetSchema])
def get_jobs(
    filters: Annotated[JobFilters, Query()],
    service: JobServiceDependency
):
    return service.get_jobs(filters)

@job_router.get("/{id}", response_model=JobGetSchema)
def get_job_by_id(
    id: int,
    service: JobServiceDependency
):
    return service.get_job_by_id(id)
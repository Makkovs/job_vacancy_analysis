from typing import Annotated, List
from fastapi import APIRouter, Query

from schemas import JobFilters, JobGetSchema, JobStatsSchema
from services import JobServiceDependency

job_router = APIRouter(prefix="/job", tags=["job"])

@job_router.get("/", response_model=List[JobGetSchema])
async def get_jobs(
    filters: Annotated[JobFilters, Query()],
    service: JobServiceDependency
):
    return await service.get_jobs(filters)

@job_router.get("/stats", response_model=JobStatsSchema)
async def get_stats(
    filters: Annotated[JobFilters, Query()],
    service: JobServiceDependency
):
    return await service.get_stats(filters)

@job_router.get("/{job_id}", response_model=JobGetSchema)
async def get_job_by_id(
    job_id: int,
    service: JobServiceDependency
):
    return await service.get_job_by_id(job_id)
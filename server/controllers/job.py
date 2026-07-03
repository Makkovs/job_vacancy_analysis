from fastapi import APIRouter, Depends

from schemas import JobFilters
from services import JobServiceDependency

job_router = APIRouter(prefix="/job", tags=["job"])

@job_router.get("/", response_model=str)
def get_jobs(
    filters: JobFilters = Depends(), 
    service: JobServiceDependency = JobServiceDependency
):
    return service.get_jobs(filters)
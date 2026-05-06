from fastapi import APIRouter

job_router = APIRouter(prefix="/job", tags=["job"])

@job_router.get("/", response_model=str)
def get_jobs():
    return "Get Jobs"
from fastapi import APIRouter

stats_router = APIRouter(prefix="/stats", tags=["stats"])

@stats_router.get("/average-salary", response_model=str)
def get_avg_salary():
    return "Get Average Salary"

@stats_router.get("/jobs_amount", response_model=str)
def get_jobs_amout():
    return "Get Jobs Amount"

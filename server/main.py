from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from controllers import *
from exception import DomainException

app = FastAPI()

@app.exception_handler(DomainException)
async def domain_exception_handler (request: Request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail" : exc.message}
    )

app.include_router(user_router)
app.include_router(stats_router)
app.include_router(skill_router)
app.include_router(resume_router)
app.include_router(job_router)
app.include_router(ai_router)
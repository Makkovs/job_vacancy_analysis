from fastapi import FastAPI

from controllers import *

app = FastAPI()

app.include_router(user_router)
app.include_router(stats_router)
app.include_router(skill_router)
app.include_router(resume_router)
app.include_router(job_router)
app.include_router(ai_router)
import os
import sys
import pandas as pd
from pydantic import TypeAdapter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db import AsyncSessionLocal
from repositories.job import JobRepository
from schemas import JobFilters, JobSchema

async def get_data():
    async with AsyncSessionLocal() as session: 
        job_repository = JobRepository(session)
        jobs = await job_repository.get_jobs(JobFilters(**{"page_size" : 1000}))
        return jobs

async def get_formatted_jobs () -> pd.DataFrame:
    jobs = await get_data()
    adapter_job = TypeAdapter(list[JobSchema])
    jobs_pydantic = adapter_job.validate_python(jobs)

    df = pd.DataFrame([job.model_dump() for job in jobs_pydantic])
    df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2
    df["salary_avg"] = df["salary_avg"].astype(int)

    skills_lists = df["skills"].apply(lambda x: [skill["name"] for skill in x])
    skill_dumies = (
        pd.get_dummies(skills_lists.explode()).groupby(level = 0).sum()
    )

    df = pd.concat([df.drop(columns=["skills"]), skill_dumies], axis = 1)
    return df
import os
import sys
import pandas as pd
from pydantic import TypeAdapter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db import AsyncSessionLocal
from repositories.job import JobRepository
from schemas import JobFilters, JobSchema, ResumeSchema

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

    df.drop("title", axis = 1, inplace = True)
    df.drop("salary_min", axis = 1, inplace = True)
    df.drop("salary_max", axis = 1, inplace = True)

    df = pd.get_dummies(df, columns = ["country"], drop_first = True, dtype = int)

    skills_lists = df["skills"].apply(lambda x: [skill["name"] for skill in x])
    skill_dumies = (
        pd.get_dummies(skills_lists.explode()).groupby(level = 0).sum()
    )

    df = pd.concat([df.drop(columns = ["skills"]), skill_dumies], axis = 1)

    answers = df["salary_avg"]
    values = df.drop(columns = "salary_avg")

    return answers, values

def format_resume (resume, feature_columns) -> pd.DataFrame:
    adapter_resume = TypeAdapter(ResumeSchema)
    resume_pydantic = adapter_resume.validate_python(resume)
    
    df = pd.DataFrame([resume_pydantic.model_dump()])
    df.drop("title", axis = 1, inplace = True)
    df.drop("description", axis = 1, inplace = True)

    skill_lists = df["skills"].apply(
        lambda x: [skill["name"] for skill in x]
    )
    skill_dummies = (
        pd.get_dummies(skill_lists.explode()).groupby(level = 0).sum()
    )

    df = pd.concat([df.drop(columns = ["skills"]), skill_dummies], axis = 1)
    df = pd.get_dummies(df, columns = ["country"], drop_first = True, dtype = int)
    df_aligned = df.reindex(columns = feature_columns, fill_value = 0)

    return df_aligned
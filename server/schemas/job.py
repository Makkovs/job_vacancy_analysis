from pydantic import BaseModel

from schemas.skill import SkillSchema

class JobFilters(BaseModel):
    skills: list[SkillSchema] | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    country: str | None = None
    qualification: str | None = None
    experience: int | None = None

class Job (BaseModel):
    title: str
    description: str
    salary_min: int
    salary_max: int
    country: str
    qualification: str
    experience: str
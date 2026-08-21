from pydantic import BaseModel

from schemas.skill import SkillSchema

class JobFilters(BaseModel):
    skill_ids: list[int] | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    country: str | None = None
    qualification: str | None = None
    experience: int | None = None

class JobSchema (BaseModel):
    title: str
    salary_min: int
    salary_max: int
    country: str
    qualification: str
    experience: int
    skills: list[SkillSchema]
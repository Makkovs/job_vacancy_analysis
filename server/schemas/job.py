from pydantic import BaseModel, ConfigDict

from schemas.skill import SkillSchema

class JobFilters(BaseModel):
    skill_ids: list[int] | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    country: str | None = None
    qualification: int | None = None
    experience: int | None = None
    page: int | None = 1
    page_size: int | None = 15

class JobSchema (BaseModel):
    title: str
    salary_min: int
    salary_max: int
    country: str
    qualification: int
    experience: int
    skills: list[SkillSchema] = []

    model_config = ConfigDict(from_attributes=True)

class JobGetSchema(JobSchema):
    id: int
    title: str
    salary_min: int
    salary_max: int
    country: str
    qualification: int
    experience: int
    skills: list[SkillSchema] = []
    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel, ConfigDict, Field, PositiveInt

from schemas.skill import SkillSchema

class JobFilters(BaseModel):
    skill_ids: list[PositiveInt] | None = None
    salary_min: PositiveInt | None = None
    salary_max: PositiveInt | None = None
    country: str | None = None
    qualification: int | None = None
    experience: int | None = None
    page: int | None = 1
    page_size: int | None = 15

class JobSchema (BaseModel):
    title: str = Field(min_length=2, max_length=255)
    salary_min: PositiveInt
    salary_max: PositiveInt
    country: str = Field(min_length=2, max_length=255)
    qualification: int
    experience: int
    skills: list[SkillSchema] = []

    model_config = ConfigDict(from_attributes=True)

class JobGetSchema(JobSchema):
    id: PositiveInt
    title: str = Field(min_length=2, max_length=255)
    salary_min: PositiveInt
    salary_max: PositiveInt
    country: str = Field(min_length=2, max_length=255)
    qualification: int
    experience: int
    skills: list[SkillSchema] = []
    model_config = ConfigDict(from_attributes=True)
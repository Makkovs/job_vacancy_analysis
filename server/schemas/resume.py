from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field, PositiveInt
from schemas import SkillSchema

class ResumeSchemaCreate (BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=5000)
    country: str = Field(min_length=2, max_length=255)
    qualification: int
    experience: int
    skill_ids: List[PositiveInt] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)

class ResumeSchema (BaseModel):
    id: PositiveInt
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=5000)
    country: str = Field(min_length=2, max_length=255)
    qualification: int
    experience: int
    skills: list[SkillSchema] = []

    model_config = ConfigDict(from_attributes=True)

class ResumeSchemaUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    qualification: int = None
    experience: int = None
    skill_ids: Optional[list[int]] = None
    country: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

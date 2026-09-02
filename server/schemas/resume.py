from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from schemas import SkillSchema

class ResumeSchemaCreate (BaseModel):
    title: str
    description: str
    skill_ids: List[int]

    model_config = ConfigDict(from_attributes=True)

class ResumeSchema (BaseModel):
    id: int
    title: str
    description: str
    skills: list[SkillSchema] = []

    model_config = ConfigDict(from_attributes=True)

class ResumeSchemaUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    skill_ids: Optional[list[int]] = None

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel

class SkillSchema(BaseModel):
    id: int
    name: str
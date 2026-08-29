from pydantic import BaseModel, ConfigDict

class SkillSchema(BaseModel):
    id: int | None = None
    name: str

    model_config = ConfigDict(from_attributes=True)
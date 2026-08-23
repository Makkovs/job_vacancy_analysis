from pydantic import BaseModel, ConfigDict

class SkillSchema(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)
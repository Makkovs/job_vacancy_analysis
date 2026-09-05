from pydantic import BaseModel, ConfigDict, Field, PositiveInt

class SkillSchema(BaseModel):
    id: PositiveInt | None 
    name: str = Field(..., min_length=1, max_length=50)

    model_config = ConfigDict(from_attributes=True)
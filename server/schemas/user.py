from pydantic import BaseModel, Field, EmailStr, PositiveInt, ConfigDict

class UserAuthSchema(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    password: str = Field(..., max_length=255)

class UserSchema (BaseModel):
    id: PositiveInt
    email: EmailStr = Field(..., max_length=255)

    model_config = ConfigDict(from_attributes=True)
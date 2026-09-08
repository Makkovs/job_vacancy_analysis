from typing import List
from fastapi import APIRouter

from schemas import SkillSchema
from services import SkillServiceDependency

skill_router = APIRouter(prefix="/skill", tags=["skill"])

@skill_router.get("/", response_model=List[SkillSchema])
async def get_skills(service: SkillServiceDependency):
    return await service.get_skills()
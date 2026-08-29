from fastapi import APIRouter
from typing import List

from schemas import SkillSchema
from services import SkillServiceDependency
skill_router = APIRouter(prefix="/skill", tags=["skill"])

@skill_router.get("/", response_model=List[SkillSchema])
def get_skills(service: SkillServiceDependency):
    return service.get_skills()
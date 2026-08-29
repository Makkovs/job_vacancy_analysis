from fastapi import Depends
from typing import List, Annotated

from models import Skill
from repositories import SkillRepositoryDependency

class SkillService:

    def __init__(self, skill_repository: SkillRepositoryDependency):
        self.repository = skill_repository

    def get_skills(self) -> List[Skill]:
        skills = self.repository.get_skills()
        return skills

SkillServiceDependency = Annotated[SkillService, Depends(SkillService)]
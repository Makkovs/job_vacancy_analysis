from fastapi import Depends
from sqlalchemy import select
from typing import Annotated, List

from models import Skill
from repositories import BaseRepository

class SkillRepository(BaseRepository):

    def get_skills(self) -> List[Skill]:
        query = select(Skill)
        return self.db.execute(query).scalars().all()

SkillRepositoryDependency = Annotated[SkillRepository, Depends(SkillRepository)]
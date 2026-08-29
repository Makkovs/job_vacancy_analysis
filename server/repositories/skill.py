from typing import Annotated
from sqlalchemy import select
from fastapi import Depends
from models import Skill
from repositories import BaseRepository

class SkillRepository(BaseRepository):

    def get_skills(self):
        query = select(Skill)
        return self.db.execute(query).scalars().all()

SkillRepositoryDependency = Annotated[SkillRepository, Depends(SkillRepository)]
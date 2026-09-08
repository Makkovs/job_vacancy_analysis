from fastapi import Depends
from sqlalchemy import select
from typing import Annotated, List

from models import Skill
from repositories import BaseRepository

class SkillRepository(BaseRepository):

    async def get_skills(self) -> List[Skill]:
        query = select(Skill)
        return (await self.db.scalars(query)).all()

SkillRepositoryDependency = Annotated[SkillRepository, Depends(SkillRepository)]
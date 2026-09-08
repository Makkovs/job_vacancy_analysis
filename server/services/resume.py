from fastapi import Depends
from typing import Annotated, List

from models import Resume
from schemas import ResumeSchemaUpdate
from exception import ResumeNotFoundError
from utils.access_token import verify_access_token
from repositories import ResumeRepositoryDependency

class ResumeService:
    def __init__(self, resume_repository: ResumeRepositoryDependency):
        self.repository = resume_repository

    async def create_resume(self, resume, token) -> Resume:
        user = verify_access_token(token)
        return await self.repository.create_resume(resume, user["id"])

    async def get_resumes(self, token) -> List[Resume]:
        user = verify_access_token(token)
        return await self.repository.get_resumes(user["id"])

    async def get_resume_by_id(self, resume_id, token) -> Resume:
        user = verify_access_token(token)   
        resume = await self.repository.get_resume_by_id(resume_id, user["id"])
        if resume is None:
            raise ResumeNotFoundError(resume_id)

        return resume

    async def delete_resume(self, resume_id, token) -> str:
        user = verify_access_token(token)
        resume = await self.repository.get_resume_by_id(resume_id, user["id"])
        if not resume:
            raise ResumeNotFoundError(resume_id)
        
        await self.repository.delete_resume(resume)
        return f"Resume with id {resume_id} was deleted!"

    async def patch_resume(self, resume_id, resume: ResumeSchemaUpdate, token) -> Resume:
        user = verify_access_token(token)
        return await self.repository.patch_resume(resume_id, user["id"], resume)

ResumeServiceDependency = Annotated[ResumeService, Depends(ResumeService)]

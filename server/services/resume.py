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

    def create_resume(self, resume, token) -> Resume:
        user = verify_access_token(token)
        return self.repository.create_resume(resume, user["id"])

    def get_resumes(self, token) -> List[Resume]:
        user = verify_access_token(token)
        return self.repository.get_resumes(user["id"])

    def get_resume_by_id(self, resume_id, token) -> Resume:
        user = verify_access_token(token)   
        resume = self.repository.get_resume(resume_id, user["id"])
        if resume is None:
            raise ResumeNotFoundError(resume_id)

        return resume

    def delete_resume(self, resume_id, token) -> str:
        user = verify_access_token(token)
        self.repository.delete_resume(resume_id, user["id"])
        return f"Resume with id {resume_id} was deleted!"

    def patch_resume(self, resume_id, resume: ResumeSchemaUpdate, token) -> Resume:
        user = verify_access_token(token)
        return self.repository.patch_resume(resume_id, user["id"], resume)

ResumeServiceDependency = Annotated[ResumeService, Depends(ResumeService)]

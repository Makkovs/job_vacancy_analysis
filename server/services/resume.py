from typing import Annotated
from fastapi import Depends
from schemas import ResumeSchema, ResumeSchemaUpdate
from repositories import ResumeRepositoryDependency
from utils.access_token import verify_access_token

class ResumeService:
    def __init__(self, resume_repository: ResumeRepositoryDependency):
        self.repository = resume_repository

    def create_resume(self, resume, token):
        user = verify_access_token(token)
        resume = self.repository.create_resume(resume, user["id"])
        return resume

    def get_resumes(self, token):
        user = verify_access_token(token)
        resumes = self.repository.get_resumes(user["id"])
        return resumes

    def get_resume_by_id(self, token, id):
        user = verify_access_token(token)
        resume = self.repository.get_resume(id, user["id"])
        return resume

    def delete_resume(self, token, id):
        user = verify_access_token(token)
        self.repository.delete_resume(id, user["id"])
        return f"Resume with id {id} was deleted!"

    def patch_resume(self, token, resume_id, resume: ResumeSchemaUpdate):
        user = verify_access_token(token)
        resume = self.repository.patch_resume(resume_id, user["id"], resume)
        return resume

ResumeServiceDependency = Annotated[ResumeService, Depends(ResumeService)]

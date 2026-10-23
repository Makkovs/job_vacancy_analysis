import json
from fastapi import Depends
from typing import Annotated, List

from models import Resume
from schemas import ResumeSchemaUpdate
from exception import ResumeNotFoundError
from utils.access_token import verify_access_token
from repositories import ResumeRepositoryDependency

from ai.model import Model
from ai.data_format import format_resume

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

    async def predict_salary(self, resume_id, token) -> int:
        user = verify_access_token(token)
        resume = await self.repository.get_resume_by_id(resume_id, user["id"])
        if not resume:
            raise ResumeNotFoundError(resume_id)

        model = Model()
        model.load_weights()

        data = format_resume(resume, model.feature_columns)
        predict = int(model.predict(data)[0])
        return predict
        
    async def offer_skill(self, resume_id, token):
        user = verify_access_token(token)
        resume = await self.repository.get_resume_by_id(resume_id, user["id"])
        if not resume:
            raise ResumeNotFoundError(resume_id)

        skills_to_learn = set()
        with open("skills_correlation.json", "r", encoding="utf-8") as f:
            skills_matrix = json.load(f)
            skills = [skill.name for skill in resume.skills]

            for skill in skills:
                for exist in skills:
                    if exist in skills_matrix[skill]:
                        del skills_matrix[skill][exist]

                max_value = max(skills_matrix[skill].values())
                max_skills = [key for key, value in skills_matrix[skill].items() if max_value - value <= 0.03]
                skills_to_learn.update(max_skills)

        return list(skills_to_learn)
        

ResumeServiceDependency = Annotated[ResumeService, Depends(ResumeService)]

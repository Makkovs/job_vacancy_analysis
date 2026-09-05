from typing import List
from fastapi import APIRouter, Header

from exception import UnauthorizedError
from services import ResumeServiceDependency
from schemas import ResumeSchema, ResumeSchemaCreate, ResumeSchemaUpdate

resume_router = APIRouter(prefix="/resume", tags=["resume"])

@resume_router.post("/create", response_model=ResumeSchema)
def create_resume(
    resume: ResumeSchemaCreate,
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):
    if not authorization:
        raise UnauthorizedError()
    token = authorization.split(" ")[1]
    return service.create_resume(resume, token)

@resume_router.get("/get", response_model=List[ResumeSchema])
def get_resumes(
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):
    if not authorization:
        raise UnauthorizedError()
    token = authorization.split(" ")[1]
    return service.get_resumes(token)

@resume_router.get("/get/{resume_id}", response_model=ResumeSchema)
def get_resume_by_id(
    resume_id: int,
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):
    if not authorization:
        raise UnauthorizedError()
    token = authorization.split(" ")[1]
    return service.get_resume_by_id(resume_id, token)

@resume_router.delete("/{resume_id}", response_model=str)
def delete_resume(
    resume_id: int,
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):  
    if not authorization:
        raise UnauthorizedError() 
    token = authorization.split(" ")[1]
    return service.delete_resume(resume_id, token)

@resume_router.patch("/patch/{resume_id}", response_model=ResumeSchema)
def patch_resume(
    resume_id: int,
    resume: ResumeSchemaUpdate,
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):
    if not authorization:
        raise UnauthorizedError()
    token = authorization.split(" ")[1]
    return service.patch_resume(resume_id, resume, token)
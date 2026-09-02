from fastapi import APIRouter, Header, HTTPException, status
from typing import List
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
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = authorization.split(" ")[1]
    return service.create_resume(resume, token)

@resume_router.get("/get", response_model=List[ResumeSchema])
def get_resumes(
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = authorization.split(" ")[1]
    return service.get_resumes(token)

@resume_router.get("/get/{id}", response_model=ResumeSchema)
def get_resume_by_id(
    id: int,
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = authorization.split(" ")[1]
    return service.get_resume_by_id(token, id)

@resume_router.delete("/{id}", response_model=str)
def delete_resume(
    id: int,
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
): 
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = authorization.split(" ")[1]
    return service.delete_resume(token, id)

@resume_router.patch("/patch/{resume_id}", response_model=ResumeSchema)
def patch_resume(
    resume_id: int,
    resume: ResumeSchemaUpdate,
    authorization: str | None = Header(None),
    service: ResumeServiceDependency = ResumeServiceDependency
):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = authorization.split(" ")[1]
    return service.patch_resume(token, resume_id, resume)
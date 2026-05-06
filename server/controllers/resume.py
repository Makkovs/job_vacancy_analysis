from fastapi import APIRouter

resume_router = APIRouter(prefix="/resume", tags=["resume"])

@resume_router.post("/create", response_model=str)
def create_resume():
    return "Create Resume"

@resume_router.get("/get", response_model=str)
def get_resumes():
    return "Get Resumes"

@resume_router.delete("/get", response_model=str)
def delete_resume():
    return "Delete Resume"

@resume_router.patch("/patch", response_model=str)
def patch_resume():
    return "Patch Resume"
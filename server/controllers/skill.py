from fastapi import APIRouter

skill_router = APIRouter(prefix="/skill", tags=["skill"])

@skill_router.post("/create", response_model=str)
def create_skill():
    return "Create Skill"

@skill_router.get("/get", response_model=str)
def get_skills():
    return "Get Skills"

@skill_router.delete("/delete", response_model=str)
def delete_skill():
    return "Delete Skill"
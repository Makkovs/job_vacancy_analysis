from fastapi import APIRouter

ai_router = APIRouter(prefix="/ai", tags=["ai"])

@ai_router.get("/predict", response_model=str)
def get_predict():
    return "Get Predict"

@ai_router.get("/recommended-skills", response_model=str)
def get_recommended_skills():
    return "Get recommended skills"

@ai_router.get("/recommendation", response_model=str)
def get_recommendation():
    return "Get recommendation"
from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/", response_model=str)
def get_user():
    return "Get User"

@user_router.post("/auth/register", response_model=str)
def create_user():
    return "Create User"

@user_router.post("/auth/login", response_model=str)
def login_user():
    return "Login User"

@user_router.post("/auth/", response_model=str)
def check_token():
    return "Check token"

@user_router.delete("/delete", response_model=str)
def delete_user():
    return "Delete User"

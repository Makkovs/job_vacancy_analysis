from fastapi import APIRouter, status, Header, HTTPException

from schemas import UserAuthSchema, UserSchema
from services import UserServiceDependency
from models import User

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/{id}", response_model=UserSchema)
def get_user(id: int, service: UserServiceDependency = UserServiceDependency) -> UserSchema:
    return service.get_user(id)

@user_router.post("/auth/register", response_model=str, status_code=status.HTTP_201_CREATED)
def create_user(user: UserAuthSchema, service: UserServiceDependency):
    return service.create_user(user=user)

@user_router.post("/auth/login", response_model=str)
def login_user(user_auth: UserAuthSchema, service: UserServiceDependency):
    return service.login_user(user_auth=user_auth)

@user_router.post("/auth/", response_model=str)
def update_token(
    authorization: str | None = Header(None), 
    service: UserServiceDependency = UserServiceDependency
) -> str:
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    token = authorization.split(" ")[1]
    return service.update_token(token)

@user_router.delete("/delete", response_model=str)
def delete_user(id: int, service: UserServiceDependency):
    return service.delete_user(id)

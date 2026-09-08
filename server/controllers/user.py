from fastapi import APIRouter, status, Header

from exception import UnauthorizedError
from services import UserServiceDependency
from schemas import UserAuthSchema, UserSchema

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/{id}", response_model=UserSchema)
async def get_user(id: int, service: UserServiceDependency) -> UserSchema:
    return await service.get_user(id)

@user_router.post("/auth/register", response_model=str, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserAuthSchema, service: UserServiceDependency):
    return await service.create_user(user=user)

@user_router.post("/auth/login", response_model=str)
async def login_user(user_auth: UserAuthSchema, service: UserServiceDependency):
    return await service.login_user(user_auth=user_auth)

@user_router.post("/auth/", response_model=str)
async def update_token(
    authorization: str | None = Header(None), 
    service: UserServiceDependency = UserServiceDependency
) -> str:
    if not authorization:
        raise UnauthorizedError
    token = authorization.split(" ")[1]
    return await service.update_token(token)

@user_router.delete("/delete/{id}", response_model=str)
async def delete_user(
    id: int, 
    authorization: str | None = Header(None),
    service: UserServiceDependency = UserServiceDependency
    ):
    if not authorization:
        raise UnauthorizedError
    token = authorization.split(" ")[1]
    return await service.delete_user(id, token)

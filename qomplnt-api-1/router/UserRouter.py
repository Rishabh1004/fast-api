from typing import List, Optional

from fastapi import APIRouter, status, Depends

from schemas.UserSchema import UserSchema,LoginSchema, Token
from services.UserService import UserService
from models.UserModel import User
from configs.Database import get_db_connection


UserRouter = APIRouter(
    prefix='/user', tags=['adarsh']
)


@UserRouter.get(
    '/',
    response_model=List[UserSchema]
)
def get(userService: UserService = Depends())->User:
    return userService.get(User())







@UserRouter.post(
    '/',
    response_model= UserSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    user: UserSchema,
    userService: UserService = Depends(),
):
    return userService.create(user)

@UserRouter.post(
    '/login',
    response_model=List[Token],
)
def login(
    user:LoginSchema,
    userService:UserService = Depends()
)->User:
    user = userService.login(user)
    return user

    # return userService.login(user)
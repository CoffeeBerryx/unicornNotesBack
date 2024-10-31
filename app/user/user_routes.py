import string

from fastapi import APIRouter

from app.user.user_controller import get_user_controller, create_user_controller, get_all_users_controller, \
    update_user_controller, delete_user_controller
from app.user.user_models import User, UserCreate

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/all")
async def get_users():
    return get_all_users_controller()


@router.get("")
async def get_user(user_id):
    return get_user_controller(user_id)


@router.post("")
async def update_user(user: User):
    return update_user_controller(user)


@router.put("")
async def create_user(user: UserCreate):
    return create_user_controller(user)


@router.delete("")
async def delete_user(user_id):
    return delete_user_controller(user_id)

from fastapi import APIRouter

from app.user.user_controller import get_user_controller, create_user_controller, get_all_users_controller

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/all")
async def get_users():
    return get_all_users_controller()

@router.get("")
async def get_user():
    return get_user_controller()

@router.post("")
async def update_user():
    return [{"method": "post user"}]

@router.put("")
async def new_user():
    return create_user_controller()

@router.delete("")
async def delete_user():
    return [{"method": "delete user"}]

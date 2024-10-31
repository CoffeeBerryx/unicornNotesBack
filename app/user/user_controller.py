import string

from fastapi import HTTPException
from sqlmodel import select

from app.user.user_models import User, UserCreate
from app.utils.sqlite_db import get_session

sqlSession = get_session()


def get_all_users_controller():
    users = sqlSession.exec(select(User)).all()
    return users


def get_user_controller(user_id):
    user = sqlSession.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def create_user_controller(user: UserCreate):
    db_user = User(name=user.name, lastName=user.lastName, age=user.age)
    sqlSession.add(db_user)
    sqlSession.commit()
    sqlSession.refresh(db_user)
    return db_user


def update_user_controller(user: User):
    user_db = sqlSession.get(User, user.id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.model_dump(exclude_unset=True)
    user_db.sqlmodel_update(user_data)
    sqlSession.add(user_db)
    sqlSession.commit()
    sqlSession.refresh(user_db)
    return user_db


def delete_user_controller(user_id):
    user = sqlSession.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    sqlSession.delete(user)
    sqlSession.commit()
    return {"ok": True}

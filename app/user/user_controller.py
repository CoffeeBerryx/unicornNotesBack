from sqlmodel import select

from app.user.user_models import User, UserCreate
from app.utils.sqlite_db import get_session
sqlSession = get_session()

def get_all_users_controller():
    users = sqlSession.exec(select(User)).all()
    return users

def get_user_controller():
    return {"method": "get user"}

def create_user_controller(user: UserCreate):
    db_user = User(name=user.name, lastName=user.lastName, age=user.age)
    sqlSession.add(db_user) #agrego el usuario
    sqlSession.commit() #hago el commit (haz la chamba)
    sqlSession.refresh(db_user) #actualizo el usuario con el nuevo id
    return db_user

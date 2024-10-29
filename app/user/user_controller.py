from sqlmodel import select

from app.user.user_models import User, UserCreate
from app.utils.sqlite_db import get_session

def get_all_users_controller():
    session = get_session()
    users = session.exec(select(User)).all()
    return users

def get_user_controller():
    return {"method": "get user"}

def create_user_controller(user: UserCreate):
    session = get_session() #necesito que me pases la conexion a la base de datos
    db_user = User(name=user.name, lastName=user.lastName, age=user.age)
    session.add(db_user) #agrego el usuario
    session.commit() #hago el commit (haz la chamba)
    session.refresh(db_user) #actualizo el usuario con el nuevo id
    return db_user
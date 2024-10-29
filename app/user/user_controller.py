from sqlmodel import select

from app.user.user_models import User
from app.utils.sqlite_db import get_session

def get_all_users_controller():
    session = get_session()
    users = session.exec(select(User)).all()
    return users

def get_user_controller():
    return {"method": "get user"}

def create_user_controller():
    user: User = User(name="John", lastName="Doe", age=30)
    session = get_session() #necesito que me pases la conexion a la base de datos
    session.add(user) #agrego el usuario
    session.commit() #hago el commit (haz la chamba)
    session.refresh(user) #actualizo el usuario con el nuevo id
    return user
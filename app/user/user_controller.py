from app.user.user_models import User
from app.utils.sqlite_db import get_session


def get_user_controller():
    return {"method": "get user"}

def create_user_controller():
    user: User = User(name="John", lastName="Doe", age=30)
    session = get_session()
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
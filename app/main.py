from fastapi import FastAPI
from .user import user_routes
from .notes import note_routes
from .utils.sqlite_db import create_db_and_tables

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(note_routes.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

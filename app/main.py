from fastapi import FastAPI
from .user import user_routes
from .utils.sqlite_db import create_db_and_tables

app = FastAPI()

app.include_router(user_routes.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
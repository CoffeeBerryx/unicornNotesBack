from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    lastName: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


class UserCreate(SQLModel):
    name: str
    lastName: str
    age: int

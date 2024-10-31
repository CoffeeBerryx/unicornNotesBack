from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default=None)
    content: str = Field(default=None)

class NoteCreate(SQLModel):
    title: str
    content: str
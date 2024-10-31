from sqlmodel import select

from app.notes.note_models import Note, NoteCreate
from app.utils.sqlite_db import get_session

def get_all_notes_controller():
    session = get_session()
    notes = session.exec(select(Note)).all()
    return notes

def get_note_controller():
    return {"method": "get note"}

def create_note_controller (note: NoteCreate):
    session = get_session() #necesito que me pases la conexion a la base de datos
    db_note = Note(title=note.title, content=note.content)
    session.add(db_note) #agrego el usuario
    session.commit() #hago el commit (haz la chamba)
    session.refresh(db_note) #actualizo el usuario con el nuevo id
    return db_note
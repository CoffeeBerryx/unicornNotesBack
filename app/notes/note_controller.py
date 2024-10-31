from fastapi import HTTPException
from sqlmodel import select

from app.notes.note_models import Note, NoteCreate
from app.utils.sqlite_db import get_session

sqlSession = get_session()

def get_all_notes_controller():
    notes = sqlSession.exec(select(Note)).all()
    return notes

def get_note_controller(note_id):
    note = sqlSession.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

def create_note_controller (note: NoteCreate):
    db_note = Note(title=note.title, content=note.content)
    sqlSession.add(db_note) #agrego el usuario
    sqlSession.commit() #hago el commit (haz la chamba)
    sqlSession.refresh(db_note) #actualizo el usuario con el nuevo id
    return db_note

def update_note_controller(note: Note):
    note_db = sqlSession.get(Note, note.id)
    if not note_db:
        raise HTTPException(status_code=404, detail="Note not found")
    note_data = note.model_dump(exclude_unset=True)
    note_db.sqlmodel_update(note_data)
    sqlSession.add(note_db)
    sqlSession.commit()
    sqlSession.refresh(note_db)
    return note_db

def delete_note_controller(note_id):
    note = sqlSession.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    sqlSession.delete(note)
    sqlSession.commit()
    return {"ok": True}
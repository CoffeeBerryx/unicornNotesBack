from fastapi import APIRouter

from app.notes.note_controller import get_note_controller, create_note_controller, get_all_notes_controller, \
     update_note_controller, delete_note_controller
from app.notes.note_models import Note, NoteCreate

router = APIRouter(prefix="/notes", tags=["Note"])

@router.get("/all")
async def get_note():
    return get_all_notes_controller()

@router.get("")
async def get_note(note_id):
    return get_note_controller(note_id)

@router.post("")
async def update_note(note: Note):
    return update_note_controller(note)

@router.put("")
async def new_note(note: NoteCreate):
    return create_note_controller(note)

@router.delete("")
async def delete_note(note_id):
    return delete_note_controller(note_id)

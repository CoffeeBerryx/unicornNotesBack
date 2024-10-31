from fastapi import APIRouter

from app.notes.note_controller import get_note_controller, create_note_controller, get_all_notes_controller
from app.notes.note_models import Note, NoteCreate

router = APIRouter(prefix="/notes", tags=["Note"])

@router.get("/all")
async def get_note():
    return get_all_notes_controller()

@router.get("")
async def get_note():
    return get_note_controller()

@router.post("")
async def update_note():
    return [{"method": "post notes"}]

@router.put("")
async def new_note(note: NoteCreate):
    return create_note_controller(note)

@router.delete("")
async def delete_note():
    return [{"method": "delete note"}]

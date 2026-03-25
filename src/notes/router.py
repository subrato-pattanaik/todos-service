"""
Router in Fastapi is used to group related endpoints together.

API router for the notes module - all /notes endpoints.
"""

from collections.abc import Sequence

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.notes.dependencies import get_db
from src.notes.models import Note
from src.notes.schemas import NoteCreate, NoteResponse, NoteUpdate
from src.notes import service

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("/", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)) -> Note:
    return service.create_note(db, note)


@router.get("/", response_model=list[NoteResponse])
def get_all_notes(db: Session = Depends(get_db)) -> Sequence[Note]:
    return service.get_all_notes(db)


@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: str, db: Session = Depends(get_db)) -> Note:
    return service.get_note_by_id(db, note_id)


@router.put("/{note_id}", response_model=NoteResponse)
def replace_note(note_id: str, note: NoteCreate, db: Session = Depends(get_db)) -> Note:
    return service.replace_note(db, note_id, note)


@router.patch("/{note_id}", response_model=NoteResponse)
def update_note(note_id: str, note: NoteUpdate, db: Session = Depends(get_db)) -> Note:
    return service.update_note(db, note_id, note)


@router.delete("/{note_id}")
def delete_note(note_id: str, db: Session = Depends(get_db)) -> dict[str, str]:
    return service.delete_note(db, note_id)

"""Business logic for the notes module."""

from collections.abc import Sequence
from sqlmodel import Session, select

from src.notes.exceptions import NoteNotFound, NoteUpdateEmpty
from src.notes.schemas import NoteCreate, NoteUpdate
from src.notes.models import Note


def create_note(db: Session, note: NoteCreate) -> Note:
    db_note = Note.model_validate(note)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_all_notes(db: Session) -> Sequence[Note]:
    return db.exec(select(Note)).all()


def get_note_by_id(db: Session, note_id: str) -> Note:
    db_note = db.get(Note, note_id)
    if not db_note:
        raise NoteNotFound(note_id)
    return db_note


def replace_note(db: Session, note_id: str, note_replace: NoteCreate) -> Note:
    db_note = db.get(Note, note_id)
    if not db_note:
        raise NoteNotFound(note_id)

    # For a PUT, we want ALL fields mapped, even if they explicitly set them to null/defaults
    update_data = note_replace.model_dump()

    for key, value in update_data.items():
        setattr(db_note, key, value)

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(db: Session, note_id: str, note_update: NoteUpdate) -> Note:
    db_note = db.get(Note, note_id)
    if not db_note:
        raise NoteNotFound(note_id)

    update_data = note_update.model_dump(exclude_unset=True)
    if not update_data:
        raise NoteUpdateEmpty()

    for key, value in update_data.items():
        setattr(db_note, key, value)

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: str) -> dict[str, str]:
    db_note = db.get(Note, note_id)
    if not db_note:
        raise NoteNotFound(note_id)

    db.delete(db_note)
    db.commit()
    return {"message": "Note deleted successfully"}

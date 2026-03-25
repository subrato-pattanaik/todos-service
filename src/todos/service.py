"""Business logic for the todos module."""

from collections.abc import Sequence
from sqlmodel import Session, select

from src.todos.exceptions import TodoNotFound, TodoUpdateEmpty
from src.todos.schemas import TodoCreate, TodoUpdate
from src.todos.models import Todo
from src.notes.models import Note


def create_todo(db: Session, todo: TodoCreate) -> Todo:
    db_todo = Todo.model_validate(todo)

    # Automatically create an empty note for this todo
    new_note = Note(title=f"Note for {db_todo.title}", content="")
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    # Link the note to the todo
    db_todo.note_id = new_note.id

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_all_todos(db: Session) -> Sequence[Todo]:
    return db.exec(select(Todo)).all()


def get_todo_by_id(db: Session, todo_id: str) -> Todo:
    db_todo = db.get(Todo, todo_id)
    if not db_todo:
        raise TodoNotFound(todo_id)
    return db_todo


def replace_todo(db: Session, todo_id: str, todo_replace: TodoCreate) -> Todo:
    db_todo = db.get(Todo, todo_id)
    if not db_todo:
        raise TodoNotFound(todo_id)

    # For a true PUT, we want ALL fields mapped, even if they explicitly set them to null/defaults
    update_data = todo_replace.model_dump()

    # Overwrite every single field on the DB object
    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: str, todo_update: TodoUpdate) -> Todo:
    db_todo = db.get(Todo, todo_id)
    if not db_todo:
        raise TodoNotFound(todo_id)

    update_data = todo_update.model_dump(exclude_unset=True)
    if not update_data:
        raise TodoUpdateEmpty()

    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)  # refresh to get new incremented id
    return db_todo


def delete_todo(db: Session, todo_id: str) -> dict[str, str]:
    db_todo = db.get(Todo, todo_id)
    if not db_todo:
        raise TodoNotFound(todo_id)

    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}

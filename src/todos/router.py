"""
Router in Fastapi is used to group related endpoints together.

API router for the todos module - all /todos endpoints.
"""

from collections.abc import Sequence

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.todos.dependencies import get_db
from src.todos.models import Todo
from src.todos.schemas import TodoCreate, TodoResponse, TodoUpdate
from src.todos import service

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)) -> Todo:
    return service.create_todo(db, todo)


@router.get("/", response_model=list[TodoResponse])
def get_all_todos(db: Session = Depends(get_db)) -> Sequence[Todo]:
    return service.get_all_todos(db)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: str, db: Session = Depends(get_db)) -> Todo:
    return service.get_todo_by_id(db, todo_id)


@router.put("/{todo_id}", response_model=TodoResponse)
def replace_todo(todo_id: str, todo: TodoCreate, db: Session = Depends(get_db)) -> Todo:
    return service.replace_todo(db, todo_id, todo)


@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: str, todo: TodoUpdate, db: Session = Depends(get_db)) -> Todo:
    return service.update_todo(db, todo_id, todo)


@router.delete("/{todo_id}")
def delete_todo(todo_id: str, db: Session = Depends(get_db)) -> dict[str, str]:
    return service.delete_todo(db, todo_id)

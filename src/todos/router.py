"""
Router in Fastapi is used to group related endpoints together.

API router for the todos module - all /todos endpoints."""

import sqlite3

from fastapi import APIRouter, Depends

from src.todos.dependencies import get_db
from src.todos.schemas import TodoCreate, TodoResponse, TodoUpdate
from src.todos import service

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, conn: sqlite3.Connection = Depends(get_db)):
    return service.create_todo(conn, todo)


@router.get("/", response_model=list[TodoResponse])
def get_all_todos(conn: sqlite3.Connection = Depends(get_db)):
    return service.get_all_todos(conn)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: str, conn: sqlite3.Connection = Depends(get_db)):
    return service.get_todo_by_id(conn, todo_id)


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: str, todo: TodoUpdate, conn: sqlite3.Connection = Depends(get_db)
):
    return service.update_todo(conn, todo_id, todo)


@router.delete("/{todo_id}")
def delete_todo(todo_id: str, conn: sqlite3.Connection = Depends(get_db)):
    return service.delete_todo(conn, todo_id)

from fastapi import APIRouter, HTTPException
from typing import List
from schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from crud.todo import todo_crud

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    return todo_crud.create(todo)

@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: str):
    todo = todo_crud.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.get("/user/{user_id}", response_model=List[TodoResponse])
async def get_user_todos(user_id: str):
    todos = todo_crud.get_by_user(user_id)
    return todos

@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: str, todo_update: TodoUpdate):
    updated_todo = todo_crud.update(todo_id, todo_update)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found or no changes made")
    return updated_todo

@router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
    if not todo_crud.delete(todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
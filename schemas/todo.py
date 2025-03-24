from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    user_id: str
    is_completed: bool = False

class TodoUpdate(TodoBase):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None

class TodoResponse(TodoBase):
    id: str
    user_id: str
    is_completed: bool

class Todo(TodoBase):
    id: str
    user_id: str
    is_completed: bool
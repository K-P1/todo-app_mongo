from schemas.todo import TodoResponse
from typing import List

def todo_serializer(todo_document) -> TodoResponse:
    return TodoResponse(
        id=str(todo_document.get("_id")),
        user_id=todo_document.get("user_id"),
        title=todo_document.get("title"),
        description=todo_document.get("description"),
        is_completed=todo_document.get("is_completed", False)
    )

def todos_serializer(todo_documents) -> List[TodoResponse]:
    return [todo_serializer(todo_document) for todo_document in todo_documents]
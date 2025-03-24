from typing import Optional, List
from bson import ObjectId
from database import Database
from schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from serializers.todo import todo_serializer, todos_serializer

class TodoCRUD:
    def __init__(self, db: Database):
        self.db = db
        self.collection = db.todo_collection

    def create(self, todo: TodoCreate) -> TodoResponse:
        todo_dict = todo.dict()
        result = self.collection.insert_one(todo_dict)
        created_todo = self.collection.find_one({"_id": result.inserted_id})
        return todo_serializer(created_todo)

    def get(self, todo_id: str) -> Optional[TodoResponse]:
        todo = self.collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(todo) if todo else None

    def get_by_user(self, user_id: str) -> List[TodoResponse]:
        todos = self.collection.find({"user_id": user_id})
        return todos_serializer(todos)

    def update(self, todo_id: str, todo_update: TodoUpdate) -> Optional[TodoResponse]:
        update_data = {k: v for k, v in todo_update.dict().items() if v is not None}
        if not update_data:
            return self.get(todo_id)
        
        result = self.collection.update_one(
            {"_id": ObjectId(todo_id)},
            {"$set": update_data}
        )
        if result.modified_count:
            return self.get(todo_id)
        return None

    def delete(self, todo_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(todo_id)})
        return result.deleted_count > 0

from database import db
todo_crud = TodoCRUD(db)
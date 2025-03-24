from typing import Optional
from datetime import datetime
from bson import ObjectId
from database import Database
from schemas.user import UserCreate, UserUpdate, UserResponse
from serializers.user import user_serializer

class UserCRUD:
    def __init__(self, db: Database):
        self.db = db
        self.collection = db.user_collection

    def create(self, user: UserCreate) -> UserResponse:
        user_dict = user.dict()
        user_dict["created_at"] = datetime.now()
        result = self.collection.insert_one(user_dict)
        created_user = self.collection.find_one({"_id": result.inserted_id})
        return user_serializer(created_user)

    def get(self, user_id: str) -> Optional[UserResponse]:
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user) if user else None

    def update(self, user_id: str, user_update: UserUpdate) -> Optional[UserResponse]:
        update_data = {k: v for k, v in user_update.dict().items() if v is not None}
        if not update_data:
            return self.get(user_id)
        
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        if result.modified_count:
            return self.get(user_id)
        return None

    def delete(self, user_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

from database import db
user_crud = UserCRUD(db)
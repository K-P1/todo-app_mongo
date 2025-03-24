from schemas.user import UserResponse
from typing import List

def user_serializer(user_document) -> UserResponse:
    """Convert a MongoDB user document to a UserResponse model."""
    return UserResponse(
        id=str(user_document.get("_id")),
        username=user_document.get("username"),
        created_at=user_document.get("created_at")
    )

def users_serializer(user_documents) -> List[UserResponse]:
    """Convert a list of MongoDB user documents to a list of UserResponse models."""
    return [user_serializer(user_document) for user_document in user_documents]
from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserUpdate, UserResponse
from user import user_crud

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    return user_crud.create(user)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = user_crud.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UserUpdate):
    updated_user = user_crud.update(user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    return updated_user

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    if not user_crud.delete(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
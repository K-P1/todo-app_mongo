from datetime import datetime
from pydantic import BaseModel
from typing import Union

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass  

class UserUpdate(UserBase):
    username: str | None = None  

class UserResponse(UserBase):
    id: str
    created_at: Union[datetime, str]

class User(UserBase):
    id: str
    created_at: Union[datetime, str] = datetime.now()
from fastapi import APIRouter
from pydantic import BaseModel
from db.models import Users



router = APIRouter()


class CreateUserRequest(BaseModel):
    id : int
    email : str
    username : str
    first_name : str
    last_name : str
    hashed_password : str
    is_active : bool
    role : str

@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = Users(
        
    )


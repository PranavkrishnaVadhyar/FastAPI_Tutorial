from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from db.models import Todos
from db.database import SessionLocal
from pydantic import BaseModel, Field
from typing import Annotated
from sqlalchemy.orm import Session
from .auth import get_current_user


router = APIRouter(prefix='/admin', tags=['admin'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # db closes after each action

# Dependency injection: Since this function relies on db, then execution begins only after executing get_db
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'Admin':
        if user is None:
            raise HTTPException(status_code=401, detail='Could not validate user')
        return db.query(Todos).all()
    
    
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status
from todoapp.models import Base, Todos
from todoapp.database import engine, SessionLocal
from pydantic import BaseModel, Field
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # db closes after each action

# Dependency injection: Since this function relies on db, then execution begins only after executing get_db
db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):       
    return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, )
    complete: bool


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())

    db.add(todo_model)
    db.commit()

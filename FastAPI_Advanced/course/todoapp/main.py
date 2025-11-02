from fastapi import FastAPI
from db.models import Base
from db.database import engine
from routers import auth
from routers import todos

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)



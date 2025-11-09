from fastapi import FastAPI
from db.models import Base
from db.database import engine
from routers import auth
from routers import todos, admin, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)




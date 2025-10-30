from fastapi import FastAPI
from todoapp.models import Base
from todoapp.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
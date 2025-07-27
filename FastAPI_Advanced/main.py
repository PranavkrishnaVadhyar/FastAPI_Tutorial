from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def read_root():

    return {"message" : "Hello world"}

@app.get('/greet/{name}') # Dynamic URL
async def greet_name(name:str, age:int) -> dict:

    return {'messsge' : f"Hello {name} {age}"}

class BookCreateModel(BaseModel):
    title : str
    author : str


@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    
    return {
        "title" : book_data.title,
        "author" : book_data.author
    } 

@app.get('/get')
async def 
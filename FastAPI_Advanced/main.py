from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()


@app.get('/')
async def read_root():

    return {"message" : "Hello world"}


class BookCreateModel(BaseModel):
    title : str
    author : str
 
class Book(BaseModel):
    id : int
    title : str
    author : str
    page_count : int

@app.get('/books', response_model=List[Book])
async def get_all_books():
    
    try:
        with open('data.json', "r") as f:
            data = json.load(f)
        
        return {'data' : data}
    
    except FileNotFoundError:
        return {'error' : 'File not found!'} 
    


@app.get('/books/{bookid}')
async def get_books(book_id:int) -> dict:
    pass

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book):
    
    with open('data.json', 'w') as f:
        
        data = json.dump(f, book_data.model_dump_json)

    if not data:
        return {'error' : 'Not added'}
    
    return {'message' : 'suceess', 'data' : book_data.model_dump_json}
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"data" : 'blog_list'}


@app.get('/blog/{id}')
def show(id : int):
    return {'data' : id}



"""
1. FastAPI Application Setup
- How to initialize a FastAPI application using `FastAPI()`.
- Overview of the `app.include_router` method to organize routes.
- Setting up a basic root endpoint.

2. Routing in FastAPI
- Using `@app.get()` to define an endpoint.
- Returning JSON responses directly from routes.
- Handling HTTP GET requests.

3. Project Modularity
- Splitting the project into modules for scalability.
- Importing and including routes from `routes.py`.

Usage in Code
- `FastAPI()` is used to create the application instance.
- `include_router(router)` is used to include modular routes.
- A root route is defined for testing the server.
"""


from fastapi import FastAPI
#from app.routes import router

app = FastAPI()

#app.include_router(router)

@app.get("/")

def root():
    return {"message": "Welcome to the To-Do List API!"}

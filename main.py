from fastapi import FastAPI
from routers import todo, user

app = FastAPI(
    title="Todo App API",
    description="A simple todo application API",
    version="1.0.0"
)

app.include_router(todo.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo App API"}
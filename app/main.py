from fastapi import FastAPI
from app.api.calculator import router as calculator_router

app = FastAPI()

app.include_router(calculator_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator!"}
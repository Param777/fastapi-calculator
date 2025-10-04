from fastapi import APIRouter

router = APIRouter()

@router.get("/add")
def add(x: float, y: float):
    return {"result": x + y}

@router.get("/subtract")
def subtract(x: float, y: float):
    return {"result": x - y}

@router.get("/multiply")
def multiply(x: float, y: float):
    return {"result": x * y}

@router.get("/divide")
def divide(x: float, y: float):
    if y == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": x / y}
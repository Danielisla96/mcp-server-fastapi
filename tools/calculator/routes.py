from fastapi import APIRouter
from .models import MultiplicationResult

router = APIRouter(prefix="/calculator", tags=["Calculadora"])


@router.get("/multiply", response_model=MultiplicationResult, operation_id="multiply_numbers")
async def multiply(a: float, b: float):
    """Multiplica dos números y devuelve el resultado."""
    product = a * b
    return {"result": product, "description": f"El producto de {a} y {b} es {product}."}
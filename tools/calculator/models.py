from pydantic import BaseModel


class MultiplicationResult(BaseModel):
    result: float
    description: str
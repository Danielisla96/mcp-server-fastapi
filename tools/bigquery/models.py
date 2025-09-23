from pydantic import BaseModel
from typing import List, Dict, Any


class BigQueryRequest(BaseModel):
    query: str


class DryRunResult(BaseModel):
    bytes_processed: int
    gigabytes_processed: float
    terabytes_processed: float
    cost_usd_estimate: str
    message: str


class QueryResult(BaseModel):
    row_count: int
    results: List[Dict[str, Any]]
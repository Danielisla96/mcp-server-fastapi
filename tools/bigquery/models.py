from pydantic import BaseModel
from typing import List, Dict, Any, Optional


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


class TableSchemaRequest(BaseModel):
    project_id: str
    dataset_id: str
    table_id: str


class ColumnSchema(BaseModel):
    name: str
    type: str
    mode: str
    description: Optional[str] = None


class TableSchemaResult(BaseModel):
    project_id: str
    dataset_id: str
    table_id: str
    columns: List[ColumnSchema]
    num_rows: Optional[int] = None
    size_bytes: Optional[int] = None
    created: Optional[str] = None
    modified: Optional[str] = None
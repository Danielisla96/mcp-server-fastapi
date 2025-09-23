from fastapi import APIRouter, HTTPException
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPICallError
from .models import BigQueryRequest, DryRunResult, QueryResult

router = APIRouter(prefix="/bigquery", tags=["BigQuery"])


@router.post(
    "/estimate-cost",
    response_model=DryRunResult,
    operation_id="estimate_bigquery_cost",
    summary="Estima el costo de una query en BigQuery (Dry Run)"
)
async def estimate_bigquery_cost(request: BigQueryRequest):
    """
    Realiza una ejecución de prueba (dry run) de una query en BigQuery para estimar la cantidad de datos que procesará,
    lo que permite calcular el costo antes de ejecutarla. No consume cuota ni genera costos.
    """
    try:
        client = bigquery.Client()
        
        job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
        query_job = client.query(request.query, job_config=job_config)

        bytes_processed = query_job.total_bytes_processed
        gb_processed = bytes_processed / (1024 ** 3)
        tb_processed = bytes_processed / (1024 ** 4)
        
        cost = tb_processed * 6.0
        
        return DryRunResult(
            bytes_processed=bytes_processed,
            gigabytes_processed=round(gb_processed, 4),
            terabytes_processed=round(tb_processed, 6),
            cost_usd_estimate=f"${cost:.4f}",
            message="Estimación completada exitosamente."
        )
    except GoogleAPICallError as e:
        raise HTTPException(status_code=400, detail=f"Error de BigQuery: {e.message}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Un error inesperado ocurrió: {str(e)}")


@router.post(
    "/execute-query",
    response_model=QueryResult,
    operation_id="execute_bigquery_query",
    summary="Ejecuta una query en BigQuery y devuelve los resultados."
)
async def execute_bigquery_query(request: BigQueryRequest):
    """
    Ejecuta una query SQL en Google BigQuery y retorna los resultados en formato JSON.
    Esta acción puede incurrir en costos.
    """
    try:
        client = bigquery.Client()
        query_job = client.query(request.query)
        results = [dict(row) for row in query_job.result()]

        return QueryResult(
            row_count=len(results),
            results=results
        )
    except GoogleAPICallError as e:
        raise HTTPException(status_code=400, detail=f"Error de BigQuery: {e.message}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Un error inesperado ocurrió: {str(e)}")
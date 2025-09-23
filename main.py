import uvicorn
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from tools.calculator.routes import router as calculator_router
from tools.pokemon.routes import router as pokemon_router
from tools.bigquery.routes import router as bigquery_router

app = FastAPI(
    title="MCP SERVER FastAPI Personalizado",
    description="Una API con herramientas de calculadora, Pokémon y Google BigQuery.",
    version="1.1.0",
)

app.include_router(calculator_router)
app.include_router(pokemon_router)
app.include_router(bigquery_router)

mcp = FastApiMCP(
    app,
    name="Servidor MCP FastAPI Personalizado",
    description="Contiene herramientas de cálculo, Pokémon y para interactuar con Google BigQuery.",
)
mcp.mount_http()

if __name__ == "__main__":
    print("Servidor de herramientas ejecutándose en http://localhost:8000")
    print("El servidor MCP está disponible en http://localhost:8000/mcp")
    print("\nHerramientas disponibles:")
    print(" - Multiplicación (GET /calculator/multiply)")
    print(" - Buscador Pokémon (GET /pokemon/{name})")
    print(" - Estimar Costo BigQuery (POST /bigquery/estimate-cost)")
    print(" - Ejecutar Query BigQuery (POST /bigquery/execute-query)")
    uvicorn.run(app, host="0.0.0.0", port=8000)
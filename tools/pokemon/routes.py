import httpx
from fastapi import APIRouter, HTTPException
from tools.shared.models import PokemonInfo

router = APIRouter(prefix="/pokemon", tags=["Pokémon"])


@router.get("/{name}", response_model=PokemonInfo, operation_id="get_pokemon_info")
async def get_pokemon_info(name: str):
    """Obtiene información de un Pokémon desde la PokeAPI."""
    api_url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
    
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"Pokémon '{name}' no encontrado.")
    
    response.raise_for_status()
    data = response.json()
    pokemon_types = [t['type']['name'] for t in data['types']]
    
    return PokemonInfo(
        id=data['id'], 
        name=data['name'], 
        weight=data['weight'], 
        types=pokemon_types
    )
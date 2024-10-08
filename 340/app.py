from typing import Dict, List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


@app.post("/", status_code=201)
async def create_food(food: Food):
    """Endpoint from Bite 03"""
    foods[food.id] = food
    return food


@app.get("/", response_model=List[Food])
async def read_foods():
    """Endpoints from Bite 04"""
    return list(foods.values())


@app.get("/{food_id}", response_model=Food)
async def read_food(food_id: int):
    """Endpoints from Bite 04"""
    return foods[food_id]


# Create the update and delete endpoints here ...
@app.put("/{id}", status_code=status.HTTP_200_OK)
async def update_food(id: int, item: Food) -> Food:
    if id in foods.keys():
        foods[id] = item
        return foods[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Food not found"
        )


@app.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_food(id: int):
    if id in foods.keys():
        del foods[id]
        return {"ok": True}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Food not found"
        )

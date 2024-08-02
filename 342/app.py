from datetime import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll export authentication further in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    id: int
    username: str
    password: str

    def __init__(self, **data: Any):
        data["password"] = get_password_hash(data["password"])
        super().__init__(**data)


class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        return self.food.kcal_per_serving * self.number_servings


app = FastAPI()
food_log: Dict[int, FoodEntry] = {}

# We've hidden the previous Food CRUD to keep it compact and to force you to
# repeat the API building process (deliberate practice is key!)


# Create CRUD endpoints for FoodEntry below as per instructions in the Bite ...
@app.post("/", status_code=201)
def add_food(food_entry: FoodEntry) -> FoodEntry:
    food_log[food_entry.id] = food_entry
    return food_entry


@app.get("/users/{userid}", status_code=200)
def get_foods_for_user(userid: int) -> List[FoodEntry]:
    return [
        food_entry for _, food_entry in food_log.items() if food_entry.user.id == userid
    ]


@app.put("/{entry_id}", status_code=200)
def replace_food_entry(entry_id: int, new_food_entry: FoodEntry) -> FoodEntry:
    if entry_id in food_log.keys():
        food_log[entry_id] = new_food_entry
        return new_food_entry
    else:
        raise HTTPException(status_code=404, detail="Food entry not found")


@app.delete("/{entry_id}", status_code=200)
def delete_food_entry(entry_id: int) -> Dict:
    if entry_id in food_log.keys():
        del food_log[entry_id]
        return {"ok": True}
    else:
        raise HTTPException(status_code=404, detail="Food entry not found")

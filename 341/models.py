from datetime import datetime
from typing import Any

from passlib.context import CryptContext
from pydantic import BaseModel


# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# which we'll further explore in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    """Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


# validation_error_cause
# Write the User and FoodEntry models here ...
class User(BaseModel):
    id: int
    username: str
    password: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = get_password_hash(kwargs["password"])


class FoodEntry(BaseModel):
    id: int  # (what in a DB would be the primary key)
    user: User  # (here we see that Pydantic models can be nested)
    food: Food  # (from previous Bite and provided in the template)
    date_added: datetime = datetime.now()  # (defaults to datetime.now())
    number_servings: float  # (fitness nerds can be quite exact about this)

    @property
    def total_calories(self) -> float:
        return self.number_servings * self.food.kcal_per_serving

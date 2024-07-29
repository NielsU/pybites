from pydantic import BaseModel, Field
from typing import Optional


# write a Food pydantic model
class Food(BaseModel):
    """
    Food pydantic model
    """

    id: int = Field(examples=[1])
    name: str = Field(examples=["oatmeal"])
    serving_size: str = Field(examples=["100 grams"])
    kcal_per_serving: int = Field(examples=[336])
    protein_grams: float = Field(examples=[13.2])
    fibre_grams: Optional[float] = Field(examples=[10.1], default=0)

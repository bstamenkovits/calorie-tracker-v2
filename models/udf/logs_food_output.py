import datetime
from pydantic import BaseModel


class LogsFoodData(BaseModel):
    date_added: datetime.datetime
    meal_name: str
    ingredient_name: str
    quantity: float
    serving_name: str
    serving_size_g: float
    total_weight_g : float
    total_calories_kcal: float
    total_fat_g: float
    total_carbs_g: float
    total_protein_g: float

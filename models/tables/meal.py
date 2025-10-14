from pydantic import BaseModel, Field
from util.hash import generate_technical_key
from typing import Optional


class MealData(BaseModel):
    id: Optional[str] = Field(default=None)
    name: str
    
    def model_post_init(self, __context):
        """Called after model initialization to set computed fields"""
        if self.id is None:
            self.id = generate_technical_key(self.name)


if __name__ == "__main__":
    # from interface.supabase_interface import SupabaseInterface
    # interface = SupabaseInterface()

    # from interface.database_interface import DatabaseInterface
    # interface = DatabaseInterface()

    # breakfast = MealData(name="Breakfast")
    # lunch = MealData(name="Lunch")
    # dinner = MealData(name="Dinner")
    # snack = MealData(name="Snack")

    # response = interface.insert_meal(breakfast)
    # response = interface.insert_meal(lunch)
    # response = interface.insert_meal(dinner)
    # response = interface.insert_meal(snack)

    test_meal = MealData(name="__test_meal__", id='123')
    print(test_meal)
    # response = interface.insert_meal(test_meal)

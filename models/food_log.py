import datetime
from pydantic import BaseModel, Field, computed_field
from util.hash import generate_technical_key


class FoodLogData(BaseModel):
    meal_id: str
    ingredient_id: str
    serving_id: str
    user_id: str
    quantity: float
    date_added: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @computed_field
    def id(self) -> str:
        input_str = f"{self.meal_id}{self.ingredient_id}{self.serving_id}{self.user_id}{self.date_added}{self.quantity}"
        return generate_technical_key(input_str)

    def to_dict(self):
        """Convert to dictionary with datetime as ISO string for Supabase"""
        data = self.model_dump()
        # Convert datetime to ISO format string
        data['date_added'] = self.date_added.isoformat()
        return data


if __name__ == "__main__":
    from interface.supabase_interface import SupabaseInterface
    interface = SupabaseInterface()

    test_food_log = FoodLogData(
        meal_id="f2265d0f5f6b7bc88c9fe2f877ccb9cb",
        ingredient_id="3792ae1410ce88b163504090d68881a7",
        serving_id="57f4a0789ce3ea98cd6c1211b086b8d9",
        user_id="6b62d8e38eff45aa22468bb25b59347a",
        quantity=10,
        date_added=datetime.datetime(3000, 1, 1, 0, 0, 0)
    )

    response = interface.insert_food_log(test_food_log)

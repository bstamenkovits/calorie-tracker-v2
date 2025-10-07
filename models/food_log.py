import datetime
from pydantic import BaseModel, Field
from util.hash import generate_technical_key
from typing import Optional


class FoodLogData(BaseModel):
    id: Optional[str] = Field(default=None)
    meal_id: str
    ingredient_id: str
    serving_id: str
    user_id: str
    quantity: float
    date_added: datetime.datetime = Field(default_factory=datetime.datetime.now)

    def model_post_init(self, __context):
        """Called after model initialization to set computed fields"""
        if self.id is None:
            input_str = f"{self.meal_id}{self.ingredient_id}{self.serving_id}{self.user_id}{self.date_added}{self.quantity}"
            self.id = generate_technical_key(input_str)

    def to_dict(self):
        """Convert to dictionary with datetime as ISO string for Supabase"""
        data = self.model_dump()
        # Convert datetime to ISO format string
        data['date_added'] = self.date_added.isoformat()
        return data


if __name__ == "__main__":
    # from interface.supabase_interface import SupabaseInterface
    # interface = SupabaseInterface()
    from interface.database_interface import DatabaseInterface
    interface = DatabaseInterface()

    test_food_log = FoodLogData(
        meal_id="3f26a210c806e1ee052b35f6b9947c26",
        ingredient_id="3792ae1410ce88b163504090d68881a7",
        serving_id="57f4a0789ce3ea98cd6c1211b086b8d9",
        user_id="54ad13ec1f719e3f5d74d0567758663d",
        quantity=10,
        date_added=datetime.datetime(3000, 1, 1, 0, 0, 0)
    )

    response = interface.insert_food_log(test_food_log)
    print(response)

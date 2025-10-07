from pydantic import BaseModel, Field
from util.hash import generate_technical_key
from typing import Optional


class ServingData(BaseModel):
    id: Optional[str] = Field(default=None)
    ingredient_id: str
    name: str
    size_g: float

    def model_post_init(self, __context):
        """Called after model initialization to set computed fields"""
        if self.id is None:
            input_str = f"{self.ingredient_id}{self.name}{self.size_g}"
            self.id = generate_technical_key(input_str)


if __name__ == "__main__":
    # from interface.supabase_interface import SupabaseInterface
    # interface = SupabaseInterface()
    from interface import DatabaseInterface
    interface = DatabaseInterface()

    test_food_serving = ServingData(
        name="__test_food_serving__",
        ingredient_id="3792ae1410ce88b163504090d68881a7",
        size_g=100.0
    )

    response = interface.insert_serving(test_food_serving)

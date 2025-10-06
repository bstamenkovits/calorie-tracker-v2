from pydantic import BaseModel, computed_field
from util.hash import generate_technical_key


class ServingData(BaseModel):
    ingredient_id: str
    name: str
    size_g: float

    @computed_field
    def id(self) -> str:
        input_str = f"{self.ingredient_id}{self.name}{self.size_g}"
        return generate_technical_key(input_str)


if __name__ == "__main__":
    from interface.supabase_interface import SupabaseInterface
    from util.hash import generate_technical_key
    interface = SupabaseInterface()

    test_food_serving = ServingData(
        name="__test_food_serving__",
        ingredient_id="3792ae1410ce88b163504090d68881a7",
        size_g=100.0
    )

    response = interface.insert_serving(test_food_serving)

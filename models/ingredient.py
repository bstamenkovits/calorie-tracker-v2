from pydantic import BaseModel, computed_field
from util.hash import generate_technical_key


class IngredientData(BaseModel):
    name: str
    calories_kcal: float
    fat_g: float
    carbs_g: float
    protein_g: float
    type: str

    @computed_field
    def id(self) -> str:
        input_str = f"{self.name}{self.calories_kcal}{self.fat_g}{self.carbs_g}{self.protein_g}{self.type}"
        return generate_technical_key(input_str)


if __name__ == "__main__":
    from interface.supabase_interface import SupabaseInterface

    interface = SupabaseInterface()

    test_food = IngredientData(
        name="__test_food__",
        calories_kcal=100,
        fat_g=20,
        carbs_g=30,
        protein_g=10,
        type="__Test Category__"
    )

    response = interface.insert_ingredient(test_food)

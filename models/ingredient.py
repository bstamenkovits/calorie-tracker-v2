from pydantic import BaseModel, Field
from util.hash import generate_technical_key
from typing import Optional


class IngredientData(BaseModel):
    id: Optional[str] = Field(default=None)
    name: str
    calories_kcal: float
    fat_g: float
    carbs_g: float
    protein_g: float
    type: str

    def model_post_init(self, __context):
        """Called after model initialization to set computed fields"""
        if self.id is None:
            input_str = f"{self.name}{self.calories_kcal}{self.fat_g}{self.carbs_g}{self.protein_g}{self.type}"
            self.id = generate_technical_key(input_str)


if __name__ == "__main__":
    # from interface.supabase_interface import SupabaseInterface
    # interface = SupabaseInterface()
    from interface import DatabaseInterface
    interface = DatabaseInterface()

    test_food = IngredientData(
        name="__test_food__",
        calories_kcal=100,
        fat_g=20,
        carbs_g=30,
        protein_g=10,
        type="__Test Category__"
    )

    response = interface.insert_ingredient(test_food)
    print(response)

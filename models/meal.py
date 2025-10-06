from pydantic import BaseModel, computed_field
from util.hash import generate_technical_key


class MealData(BaseModel):
    name: str

    @computed_field
    def id(self) -> str:
        return generate_technical_key(self.name)


if __name__ == "__main__":
    from interface.supabase_interface import SupabaseInterface
    from util.hash import generate_technical_key
    interface = SupabaseInterface()

    breakfast = MealData(
        id=generate_technical_key("Breakfast"),
        name="Breakfast"
    )

    lunch = MealData(
        id=generate_technical_key("Lunch"),
        name="Lunch"
    )

    dinner = MealData(
        id=generate_technical_key("Dinner"),
        name="Dinner"
    )

    snack = MealData(
        id=generate_technical_key("Snack"),
        name="Snack"
    )

    response = interface.insert_meal(breakfast)
    response = interface.insert_meal(lunch)
    response = interface.insert_meal(dinner)
    response = interface.insert_meal(snack)

import streamlit as st
from supabase import Client, create_client
from models import UserData, MealData, FoodLogData, IngredientData, ServingData
from typing import Dict, Any

class SupabaseInterface:
    """
    A class to interact with Supabase (PostgreSQL) for inserting and retrieving data.

    Attributes:
        - supabase(Client) : The Supabase client instance.

    Methods:
        - insert_user(user_data: UserData) -> Dict[str, Any]
        - insert_meal(meal_data: MealData) -> Dict[str, Any]
        - insert_ingredient(ingredient_data: IngredientData) -> Dict[str, Any]
        - insert_serving(serving_data: ServingData) -> Dict[str, Any]
        - insert_food_log(food_log: FoodLogData) -> Dict[str, Any]

    Usage:
    ```python
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
    ```
    """
    def __init__(self):
        supabase_url = st.secrets["SUPABASE"]["url"]
        supabase_key = st.secrets["SUPABASE"]["api_key"]
        self.supabase: Client = create_client(supabase_url, supabase_key)

    def insert_user(self, user_data: UserData) -> Dict[str, Any]:
        """Insert a new user into the 'users' table."""
        return (
            self.supabase.table("users")
            .insert(user_data.model_dump())
            .execute()
        )

    def insert_meal(self, meal_data: MealData) -> Dict[str, Any]:
        """Insert a new meal into the 'meals' table."""
        return (
            self.supabase.table("meals")
            .insert(meal_data.model_dump())
            .execute()
        )

    def insert_ingredient(self, ingredient_data: IngredientData) -> Dict[str, Any]:
        """Insert a new ingredient into the 'ingredients' table."""
        return (
            self.supabase.table("ingredients")
            .insert(ingredient_data.model_dump())
            .execute()
        )

    def insert_serving(self, serving_data: ServingData) -> Dict[str, Any]:
        """Insert a new serving into the 'servings' table."""
        return (
            self.supabase.table("servings")
            .insert(serving_data.model_dump())
            .execute()
        )

    def insert_food_log(self, food_log: FoodLogData) -> Dict[str, Any]:
        """Insert a new food log entry into the 'food_logs' table."""
        return (
            self.supabase.table("food_logs")
            .insert(food_log.to_dict())  # custom to_dict method to handle serialization of datetime objects
            .execute()
        )



if __name__ == "__main__":
    from util.hash import generate_technical_key
    interface = SupabaseInterface()

    

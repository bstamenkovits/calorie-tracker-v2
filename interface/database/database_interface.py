from interface.database.connection import DatabaseConnection
from models import UserData, MealData, FoodLogData, IngredientData, ServingData, LogsFoodData, LogsFoodInputData
from typing import Dict, Any


class DatabaseInterface(DatabaseConnection):

    def __init__(self):
        super().__init__()

    # -------------- #
    # RETRIEVAL METHODS #
    # -------------- #
    def get_users(self) -> list[UserData]:
        """Fetch all users from the 'users' table."""
        query = "SELECT * FROM users;"
        result = self.fetch_results(query)
        return [UserData(id=id, name=name) for id, name in result]

    def get_meals(self) -> list[MealData]:
        """Fetch all meals from the 'meals' table."""
        query = "SELECT * FROM meals;"
        result = self.fetch_results(query)
        return [MealData(id=id, name=name) for id, name in result]

    def get_logs_food(self, logs_food_input_data: LogsFoodInputData) -> list[LogsFoodData]:
        """Fetch all food logs from the 'food_logs' table."""
        input_data = logs_food_input_data.to_dict()
        query = "SELECT * FROM get_logs_food(%(user_id)s, %(date_added)s);"
        result = self.fetch_results(query, input_data)
        return [LogsFoodData(
            date_added=date_added,
            meal_name=meal_name,
            ingredient_name=ingredient_name,
            quantity=quantity,
            serving_name=serving_name,
            serving_size_g=serving_size_g,
            total_weight_g=total_weight_g,
            total_calories_kcal=total_calories_kcal,
            total_fat_g=total_fat_g,
            total_carbs_g=total_carbs_g,
            total_protein_g=total_protein_g,
        ) for (
            date_added,
            meal_name,
            ingredient_name,
            quantity,
            serving_name,
            serving_size_g,
            total_weight_g,
            total_calories_kcal,
            total_fat_g,
            total_carbs_g,
            total_protein_g,
        )  in result]

    # -------------- #
    # INSERT METHODS #
    # -------------- #
    def insert_user(self, user_data: UserData) -> Dict[str, Any]:
        """Insert a new user into the 'users' table."""
        query = """
        INSERT INTO users (id, name)
        VALUES (%(id)s, %(name)s)
        RETURNING *;
        """
        data = user_data.model_dump()
        self.execute_query(query, data)
        return data

    def insert_meal(self, meal_data: MealData) -> Dict[str, Any]:
        """Insert a new meal into the 'meals' table."""
        query = """
        INSERT INTO meals (id, name)
        VALUES (%(id)s, %(name)s)
        RETURNING *;
        """
        data = meal_data.model_dump()
        self.execute_query(query, data)
        return data

    def insert_ingredient(self, ingredient_data: IngredientData) -> Dict[str, Any]:
        """Insert a new ingredient into the 'ingredients' table."""
        query = """
        INSERT INTO ingredients (id, name, calories_kcal, fat_g, carbs_g, protein_g, type)
        VALUES (%(id)s, %(name)s, %(calories_kcal)s, %(fat_g)s, %(carbs_g)s, %(protein_g)s, %(type)s)
        RETURNING *;
        """
        data = ingredient_data.model_dump()
        self.execute_query(query, data)
        return data

    def insert_serving(self, serving_data: ServingData) -> Dict[str, Any]:
        """Insert a new serving into the 'servings' table."""
        query = """
        INSERT INTO servings (id, ingredient_id, name, size_g)
        VALUES (%(id)s, %(ingredient_id)s, %(name)s, %(size_g)s)
        RETURNING *;
        """
        data = serving_data.model_dump()
        self.execute_query(query, data)
        return data

    def insert_food_log(self, food_log: FoodLogData) -> Dict[str, Any]:
        """Insert a new food log entry into the 'food_logs' table."""
        query = """
        INSERT INTO food_logs (id, meal_id, ingredient_id, serving_id, user_id, quantity, date_added)
        VALUES (%(id)s, %(meal_id)s, %(ingredient_id)s, %(serving_id)s, %(user_id)s, %(quantity)s, %(date_added)s)
        RETURNING *;
        """
        data = food_log.to_dict() # Use the custom to_dict method to handle datetime serialization
        self.execute_query(query, data)
        return data

    # -------------- #
    # REMOVE METHODS #
    # -------------- #
    def remove_user(self, user_id: str) -> Dict[str, Any]:
        """Remove a user from the 'users' table by ID."""
        query = """
        DELETE FROM users
        WHERE id = %(id)s
        RETURNING *;
        """
        data = {"id": user_id}
        self.execute_query(query, data)
        return data

    def remove_meal(self, meal_id: str) -> Dict[str, Any]:
        """Remove a meal from the 'meals' table by ID."""
        query = """
        DELETE FROM meals
        WHERE id = %(id)s
        RETURNING *;
        """
        data = {"id": meal_id}
        self.execute_query(query, data)
        return data

    def remove_ingredient(self, ingredient_id: str) -> Dict[str, Any]:
        """Remove an ingredient from the 'ingredients' table by ID."""
        query = """
        DELETE FROM ingredients
        WHERE id = %(id)s
        RETURNING *;
        """
        data = {"id": ingredient_id}
        self.execute_query(query, data)
        return data

    def remove_serving(self, serving_id: str) -> Dict[str, Any]:
        """Remove a serving from the 'servings' table by ID."""
        query = """
        DELETE FROM servings
        WHERE id = %(id)s
        RETURNING *;
        """
        data = {"id": serving_id}
        self.execute_query(query, data)
        return data

    def remove_food_log(self, food_log_id: str) -> Dict[str, Any]:
        """Remove a food log entry from the 'food_logs' table by ID."""
        query = """
        DELETE FROM food_logs
        WHERE id = %(id)s
        RETURNING *;
        """
        data = {"id": food_log_id}
        self.execute_query(query, data)
        return data


if __name__ == "__main__":
    db_interface = DatabaseInterface()
    result = db_interface.get_users()
    print(result)

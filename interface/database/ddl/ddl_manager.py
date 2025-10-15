import os
from interface.database.connection import DatabaseConnection
from models import UserData, MealData, FoodLogData, IngredientData, ServingData


class DDLManager:

    def __init__(self, connection: DatabaseConnection):
        self.connection = connection

    def create_tables(self):
        tables_dir = os.path.join(os.getcwd(), "interface", "database", "ddl", "tables")
        for table in os.listdir(tables_dir):
            if table.endswith(".sql"):
                with open(os.path.join(tables_dir, table), 'r') as file:
                    sql = file.read()
                    self.connection.execute_query(sql)

    def create_views(self):
        views_dir = os.path.join(os.getcwd(), "interface", "database", "ddl", "views")
        for view in os.listdir(views_dir):
            if view.endswith(".sql"):
                with open(os.path.join(views_dir, view), 'r') as file:
                    sql = file.read()
                    self.connection.execute_query(sql)

    def create_udfs(self):
        udfs_dir = os.path.join(os.getcwd(), "interface", "database", "ddl", "udfs")
        for udf in os.listdir(udfs_dir):
            if udf.endswith(".sql"):
                with open(os.path.join(udfs_dir, udf), 'r') as file:
                    sql = file.read()
                    self.connection.execute_query(sql)


if __name__ == "__main__":
    db_connection = DatabaseConnection()
    ddl_manager = DDLManager(db_connection)
    # ddl_manager.create_tables()
    # ddl_manager.create_views()
    ddl_manager.create_udfs()

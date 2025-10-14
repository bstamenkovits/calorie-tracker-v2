import psycopg2
import streamlit as st
from contextlib import contextmanager


class DatabaseConnection:

    def __init__(self):
        self.user = st.secrets["SUPABASE"]["user"]
        self.password = st.secrets["SUPABASE"]["password"]
        self.host = st.secrets["SUPABASE"]["host"]
        self.port = st.secrets["SUPABASE"]["port"]
        self.dbname = st.secrets["SUPABASE"]["dbname"]

    @contextmanager
    def get_connection(self):
        """Context manager for database connections"""
        connection = None
        try:
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                dbname=self.dbname
            )
            yield connection
        except Exception as e:
            if connection:
                connection.rollback()
            raise
        finally:
            if connection:
                connection.close()

    @contextmanager
    def get_cursor(self):
        """Context manager that provides both connection and cursor"""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                yield cursor

    def execute_query(self, query: str, params=None):
        """Execute a query that modifies the database (INSERT, UPDATE, DELETE)"""
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            cursor.connection.commit()

    def fetch_results(self, query: str, params=None):
        """Fetch results from a SELECT query"""
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

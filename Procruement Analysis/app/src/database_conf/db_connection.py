import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    """
    A class to handle database connections using the configuration provided in .env.
    """
    def __init__(self):
        self.conn_str = os.getenv("DATABASE_URL")

        if not self.conn_str:
            raise ValueError("DATABASE_URL must be set in the .env file.")

    def get_connection(self):
        """
        Establishes and returns a database connection.
        """
        try:
            connection = pyodbc.connect(self.conn_str)
            return connection
        except pyodbc.Error as e:
            raise Exception(f"Database connection error: {e}")

    def execute_query(self, query, params=None):
        """
        Executes a query with optional parameters.
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params or [])
                conn.commit()
        except pyodbc.Error as e:
            raise Exception(f"Error executing query: {e}")

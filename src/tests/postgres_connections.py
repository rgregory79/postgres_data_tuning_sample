import psycopg2
from psycopg2 import sql

class PostgresConnection:
    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Example usage:
# postgres_conn = PostgresConnection(dbname="your_db", user="your_user", password="your_password", host="localhost", port=5432)
# result = postgres_conn.execute_query("SELECT * FROM your_table;")
# print(result)
# postgres_conn.close_connection() 

import unittest
from postgres_connections import PostgresConnection

class TestQueries(unittest.TestCase):
    def setUp(self):
        # Set up a connection before each test
        self.postgres_conn = PostgresConnection(dbname="your_db", user="your_user", password="your_password", host="localhost", port=5432)

    def tearDown(self):
        # Close the connection after each test
        self.postgres_conn.close_connection()

    def test_select_all_users(self):
        query = "SELECT * FROM users;"
        result = self.postgres_conn.execute_query(query)
        # Add assertions based on the expected result

    def test_select_orders_by_user(self):
        user_id = 1
        query = "SELECT * FROM orders WHERE user_id = %s;"
        result = self.postgres_conn.execute_query(query, (user_id,))
        # Add assertions based on the expected result

if __name__ == "__main__":
    unittest.main()


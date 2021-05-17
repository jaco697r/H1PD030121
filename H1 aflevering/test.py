import unittest
import sqlite3
from utils import basket

class MyTest(unittest.TestCase):
    # Test if create_basket method returns basket id 1 when input is customerID 1
    def test(self):
        connection=sqlite3.connect("db.db")
        self.assertEqual(basket.create_basket(1, connection), 1)
        connection.close()

if __name__ == '__main__':
    unittest.main()
import unittest
import sqlite3
from main import create_basket

class MyTest(unittest.TestCase):
    # Test if create_basket method returns basket id 1 when input is customerID 1
    def test(self):
        connection=sqlite3.connect("db.db")
        cursor=connection.cursor()
        self.assertEqual(create_basket(1, cursor), 1)       

if __name__ == '__main__':
    unittest.main()
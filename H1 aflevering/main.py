from sqlite3.dbapi2 import connect
from utils import customers, items, basket, basketlines, stock
import sqlite3
import os
import functools
import unittest


def login(connection):
    cursor=connection.cursor()
    while True:
        print("Press n to create a new account")
        print("Enter your customerID: ")
        user_input = input()
        if user_input.lower() == "n":
            new_customer = customers()
            c_id = new_customer.create_user(cursor, connection)
            start_menu(c_id, cursor)
        else:
            # Check if user_input is an integer.
            try:
                int_user_input = int(user_input)
            except:
                print(f"ERROR. Your customer id is a digit. Your input: {user_input} is not a digit")
            else:
                cursor.execute(f"SELECT * FROM customer WHERE (id=?)", (str(user_input),))
                c_info = cursor.fetchall()
                c_id = [x[0] for x in c_info]
                print(f"Your account info: {c_info}")
                if c_id:
                    start_menu(c_id[-1], cursor)
                else:
                    print("Customer ID not found. Try again or contact support")

# Passing cursor for unittest purpose
def start_menu(c_id, cursor):
    while True:
        print("Welcome to GODLIKE-ERP") 
        print("1. Buy products")
        print("2. See your basket")
        print("3. Add products to stock")
        print("4. See all products")
        print("5. Delete product")
        print("6. See all customers")
        print("8. Exit")
        
        user_input = input("\nWhat do you want to do?: ")
        if user_input == '1':
            basketlines.buy_products(c_id, connection)
        elif user_input == '2':
            basketlines.see_basketlines(c_id)
        elif user_input == '3':
            items.add_products(connection, cursor)
        elif user_input == '4':
            items.see_products(cursor)
        elif user_input == '5':
            items.delete_product(connection)
        elif user_input == '6':
            customers.see_customers(cursor)
        elif user_input == '8':
            connection.close()
            exit()

if __name__ == "__main__":
    try:
        connection=sqlite3.connect(os.getcwd()+"\H1 aflevering\db.db")
        # Passing connection for unittest purpose
        login(connection)
    finally:
        connection.close()


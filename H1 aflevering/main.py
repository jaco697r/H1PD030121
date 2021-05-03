from utils import customers, items, basket, stock
import sqlite3
import os
import functools


def login():
    while True:
        print("Welcome to GODLIKE-ERP") 
        print("Press n to create a new account")
        print("Enter your customerID: ")
        user_input = input()
        if user_input == "n" or user_input == "N":
            create_user(user_input)
        else:
            try:
                cursor.execute(f"SELECT * FROM customer WHERE (id=?)", (user_input))
                c_id = cursor.fetchall()
                print(f"You name is: {c_id}")
            except:
                print('User id not found. Try again')

                
def create_user(user_input):   
    new_customer = customers()
    cursor.execute(f'INSERT INTO customer (firstName, lastName, phone, address, city, zipcode) VALUES ("{new_customer.first_name}", "{new_customer.last_name}", "{new_customer.phone}", "{new_customer.address}", "{new_customer.city}", {new_customer.zipcode})')
    try:
        connection.commit()
    except Exception:
        pass
    else:
        print(f"Customer \n{new_customer.first_name} {new_customer.last_name} \n{new_customer.address} \n{new_customer.city} \n{new_customer.zipcode}")
        cursor.execute(f"SELECT id FROM customer WHERE (phone=?)", (new_customer.phone,))
        c_id = cursor.fetchall()
        print("Your customer ID is your login. Please renember it.")
        print(f"Your customer ID is: {c_id}")

def start_menu():
    while True:
        print("Welcome to GODLIKE-ERP") 
        print("1. Buy products")
        print("2. Add products to stock")
        print("3. See all products")
        print("4. Add customer")
        print("5. See all customers")
        print("8. Exit")
        
        user_input = input("\nWhat do you want to do?: ")
        if user_input == '1':
            buy_products()
        elif user_input == '2':
            add_products()
        elif user_input == '3':
            see_products()
        elif user_input == '4':
            add_customer()
        elif user_input == '5':
            see_customers()
        elif user_input == '8':
            exit()

def buy_products():
    new_basket = basket()
    # new_basket_line = basketline()
    cursor.execute(f'INSERT INTO basket (itemnumber, customerid, quantity) VALUES ({int(new_basket.itemNumber)}, {new_basket.customerid}, "{new_basket.quantity}")')
    try:
        connection.commit()
    except Exception:
        pass

def add_products():
    new_item = items()
    amount_product_in_db = 0
    for row in cursor.execute('SELECT quantity from items WHERE name = "{}"'.format(new_item.name)):
        res = functools.reduce(lambda sub, ele: sub * 10 + ele, row)
        amount_product_in_db += res
    if amount_product_in_db > 0:
        sql_command = "REPLACE"
    else:
        sql_command = "INSERT"
    cursor.execute(f'{sql_command} INTO items (quantity, price, name) VALUES ({int(new_item.quantity) + amount_product_in_db}, {new_item.price}, "{new_item.name}")')

    amount_in_db = 0
    for row in cursor.execute('SELECT qty from stock WHERE name = "{}"'.format(new_item.name)):
        res = functools.reduce(lambda sub, ele: sub * 10 + ele, row)
        amount_in_db += res
    if amount_in_db > 0:
        sql_command = "REPLACE"
    else:
        sql_command = "INSERT"
    cursor.execute(f'{sql_command} INTO stock (qty, shelf, name) VALUES ({int(new_item.quantity) + amount_in_db}, {1}, "{new_item.name}")')

    amount_in_db = 0
    for row in cursor.execute('SELECT qty from stock WHERE name = "{}"'.format(new_item.name)):
        res = functools.reduce(lambda sub, ele: sub * 10 + ele, row)
        amount_in_db += res
    if amount_in_db > 0:
        sql_command = "REPLACE"
    else:
        sql_command = "INSERT"
    # cursor.execute(f'{sql_command} INTO stock (stockid) VALUES ({})')

    try:
        connection.commit()
    except Exception:
        pass

def see_products():
    print("ID, QTY, Price, Name")
    for row in cursor.execute('SELECT * from stock'):
        print(row)
    input('Press any key to continue')

def add_customer():
    new_customer = customers()
    existing_customer = None
    for row in cursor.execute('SELECT phone FROM customers WHERE phone = "{}"'.format(new_customer.phone)):
        res = functools.reduce(lambda sub, ele: sub * 10 + ele, row)
        existing_customer += res
    if existing_customer:
        sql_command = "REPLACE"
    else:
        sql_command = "INSERT"
    cursor.execute(f'{sql_command} INTO customers (firstname, lastname, address, phone, zipcode, city) VALUES ("{new_customer.first_name}", "{new_customer.last_name}", "{new_customer.address}", {new_customer.phone}, {new_customer.zipcode}, "{new_customer.city}")')
    try:
        connection.commit()
    except Exception:
        pass

def see_customers():
    print("ID, fName, lName, Address, Phone, ZIP, city")
    for row in cursor.execute('SELECT * from customers'):
        print(row)
    input('Press any key to continue')
    

if __name__ == "__main__":
    connection=sqlite3.connect("db.db")
    cursor=connection.cursor()
    login()
    start_menu()
    connection.close()
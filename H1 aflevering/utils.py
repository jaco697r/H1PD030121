import sqlite3
from sqlite3.dbapi2 import Cursor, connect
import functools

# connection=sqlite3.connect("db.db")
# cursor=connection.cursor()

class basket():
    def __init__(self, customer_id):
        self.customerid = customer_id

    def create_basket(c_id, connection):
        cursor=connection.cursor()
        basket_id = check_integrity("SELECT", "id", "basket", "customerID", c_id)
        if basket_id:
            print(f"You already have a basket. ID: {basket_id[0][0]}")
            return basket_id[0][0]
        else:
            # Object not used? Reconsider UML
            # Creates new basket, query for it's id and return it
            new_basket = basket(c_id)
            print("NEW BASKET CREATED")
            print(c_id)
            cursor.execute(f'INSERT INTO basket (customerID) VALUES ({str(c_id)})')
            connection.commit()
            basket_id = check_integrity("SELECT", "id", "basket", "customerID", c_id)
            return basket_id[0][0]

class basketlines():
    def __init__(self, basketid):
        self.basketid = basketid
        self.productid = input("Enter Product ID")

    def buy_products(c_id, connection):
        cursor=connection.cursor()
        basket_id = basket.create_basket(c_id, connection)
        sucess = False
        while sucess == False:
            new_basket_line = basketlines(basket_id)
            # cursor.execute(f'SELECT id FROM items WHERE (id) VALUES ({str(new_basket_line.productid)})')
            p_id = check_integrity("SELECT", "*", "items", "id", new_basket_line.productid)
            if p_id:
                cursor.execute(f'INSERT INTO basketlines (productid, basketid) VALUES ({int(new_basket_line.productid)}, {basket_id})')
                connection.commit()
                print(f"Product: '{p_id[0][1]}' with price: '{p_id[0][2]}.-' added to your basket")
                sucess = True
            else:
                u_input = input(f"Product ID: {new_basket_line.productid} does not exist. Add the product to the database or try another product.\n Press q to return to main menu.\n Press any other key to try again:  ")
                if u_input.lower() == "q":
                    sucess = True 
        
class customers():
    def __init__(self):
        self.first_name = input('Enter First Name: ') 
        self.last_name = input('Enter Last Name: ')
        self.address = input("Enter Address: ")
        self.phone = input("Enter Phone: ")
        self.zipcode = input("Enter Zipcode: ")
        self.city = input("Enter City: ") 

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    def create_user(self, cursor, connection):   
        # Inputs customer info into database. If customer phone is allready in database, return customer id
        cursor.execute(f"SELECT id FROM customer WHERE (phone=?)", (self.phone,))
        existing_customer = cursor.fetchall()
        if not existing_customer:
            cursor.execute(f'INSERT INTO customer (firstName, lastName, phone, address, city, zipcode) VALUES ("{self.first_name}", "{self.last_name}", "{self.phone}", "{self.address}", "{self.city}", {self.zipcode})')
            try:
                connection.commit()
            except Exception:
                pass
            else:
                print(f"Customer \n{self.first_name} {self.last_name} \n{self.address} \n{self.city} \n{self.zipcode}")
                cursor.execute(f"SELECT id FROM customer WHERE (phone=?)", (self.phone,))
                c_id = cursor.fetchall()
                print("Customer created!")
                print("Your customer ID is your login. Please renember it.")
                print(f"Your customer ID is: {c_id[0][0]}")
                return c_id[0][0]
        else:
            c_id = [x for x in existing_customer]
            print(f"A customer with this phone number already exists. Your customer id is: {c_id}")
            return c_id[0][0]

    def see_customers(cursor):
        print("ID,  fName,   lName")
        for row in cursor.execute('SELECT * from customer'):
            print(row)
        input('Press any key to continue: ')

class stock():
    def __init__(self):
        self.quantity = input('Enter quantity: ')

class items(stock):
    def __init__(self):
        self.name = input('Enter name: ') 
        self.price = input("Enter price per unit: ")
        super().__init__()
    
    def add_products(connection, cursor):
        new_item = items()
        amount_product_in_db = 0
        # ids = check_integrity("SELECT", "id", "items", "name", new_item.name)
        # if ids:
        #     print(ids)
        for row in cursor.execute(f'SELECT id from items WHERE name = "{new_item.name}"'):
            res = functools.reduce(lambda sub, ele: sub * 10 + ele, row)
            amount_product_in_db += res
        print(amount_product_in_db)
        if amount_product_in_db > 0:
            sql_command = "REPLACE"
        else:
            sql_command = "INSERT"
        cursor.execute(f'{sql_command} INTO items (name, price) VALUES ("{new_item.name}", {new_item.price})')
        connection.commit()

        cursor.execute(f'SELECT id from items WHERE name = "{new_item.name}"')
        itemid = cursor.fetchall()
        amount_in_db = 0
        for row in cursor.execute('SELECT qty from stock WHERE itemid = "{}"'.format(itemid[0][0])):
            res = functools.reduce(lambda sub, ele: sub * 10 + ele, row)
            amount_in_db += res
        if amount_in_db > 0:
            sql_command = "REPLACE"
        else:
            sql_command = "INSERT"
        cursor.execute(f'{sql_command} INTO stock (qty, shelf, itemid) VALUES ({int(new_item.quantity) + amount_in_db}, {1}, "{itemid[0][0]}")')
        amount_in_db = 0
        for row in cursor.execute('SELECT qty from stock WHERE id = "{}"'.format(itemid)):
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

    def see_products(cursor):
        print("ID, Name, Price")
        for row in cursor.execute('SELECT * from items'):
            print(row)
        input('Press any key to continue')

class toy(items):
    def __init__(self, *args):
        if len(args)> 4:
            age_limit = 7
        else:
            age_limit = 3

def check_integrity(*args):
    connection=sqlite3.connect("db.db")
    cursor=connection.cursor()
    cursor.execute(f"{args[0]} {args[1]} FROM {args[2]} WHERE {args[3]} = {args[4]}")
    x = cursor.fetchall()
    if x:
        connection.close()
        print(x[0][0])
        return x 
    else:
        connection.close()
        return False

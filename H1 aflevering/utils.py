
class basket():
    def __init__(self):
        self.customerid = input('Enter customer ID: ') 
        self.itemNumber = input('Enter product ID: ')
        self.quantity = input('Enter quantity: ')

class basketlines():
    x = 1
        
class customers():
    def __init__(self, last_name="Not Provided"):
        self.first_name = input('Enter First Name: ') 
        self.last_name = input('Enter Last Name: ')
        self.address = input("Enter Address: ")
        self.phone = input("Enter Phone: ")
        self.zipcode = input("Enter Zipcode: ")
        self.city = input("Enter City: ")

class shelf():
    def __init__(self):
        self.shelf = input("Enter shelf number to place the product: ")

class stock(shelf):
    def __init__(self):
        self.quantity = input('Enter quantity: ')
        super().__init__()

class items(stock):
    def __init__(self):
        self.id = None
        self.name = input('Enter name: ') 
        self.price = input("Enter price per unit: ")
        super().__init__()
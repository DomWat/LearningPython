master_list = []



class Grocery_store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []

class Grocery_item:
    def __init__(self, name, price, quantity):
        self.name_item = name
        self.price_item = price
        self.quantity_item = quantity


def grocery_store_info():
    name_store = input("Name of the store: ")
    address_store = input("Address of the store: ")
    master_list.append(Grocery_store(name_store, address_store))

def grocery_item_info():
    name_item = input("Name of the items: ")
    price_item = input("Price of items: ")
    quantity_item = input("Quantity of items: ")
    master_list.append(Grocery_item(name_item, price_item, quantity_item))

def options():
    while True: 
        print("""
        1. add store
        2. add item
        3. remove item
        4. view all lists 
        f. finish
        Enter an option: 
        """ )
        answer = input("")
        if answer == "1":
            grocery_store_info()
            #break
        elif answer == "2":
            grocery_item_info()
        elif answer == "3":
            pass
        elif answer == "4":
            pass

options()
   






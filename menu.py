import csv
import shortuuid
from typing import List, Dict
from itertools import repeat
from db_helper import DBHelper
from customer import Customer

# main menu, user chooses an option 
def main_menu_choice():
    input_is_correct = False
    
    while input_is_correct == False:
        try:
            choice = int(input('\nPlease choose an option by selecting a number:\n'
                                '0) Exit this Application\n'
                                '1) See Product Menu Options\n'
                                '2) See Courier Options\n'
                                '3) See Order Options\n'
                                'Please enter a number from the options above: '))
            if (type(choice) == int and choice <= 3 and choice >= 0):
                input_is_correct = True
            else:
                print('You need to pick one of the numbers above')
        except ValueError:
            print('You need to enter one of the numbers above')
            input_is_correct = False
        except Exception as e:
            print(f'There is an error {str(e)}')
            input_is_correct = False
            
    return choice

# next menu choice, for CRUD operations for products and couriers
def sub_menu_choice(products_or_couriers):
    input_is_correct = False;
    while input_is_correct == False:
        try:
            choice = int(input('\nPlease choose an option by selecting a number:\n'
                                '0) Return to previous menu\n'
                                f'1) Add a {products_or_couriers}\n'
                                f'2) View all {products_or_couriers}s\n'
                                f'3) Update a {products_or_couriers}\n'
                                f'4) Delete a {products_or_couriers}\n'
                                'Please select a number from the above options: '))
            if (type(choice) == int and choice <=4 and choice >=0):
                input_is_correct = True
            else:
                print('You need to pick one of the numbers above')
        except ValueError:
            print('You need to enter one of the numbers above')
            input_is_correct = False
        except Exception as e:
            print(f'There is an error {str(e)}')
            input_is_correct = False

    return choice

def view_orders_choice():
    input_is_correct = False;
    while input_is_correct == False:
        try:
            choice = int(input('\nPlease choose an option by selecting a number:\n'
                                '1 - View all orders\n'
                                '2 - View orders by status\n'
                                '3 - View orders by courier\n'
                                ))
            if (type(choice) == int and choice <=3 and choice >=1):
                input_is_correct = True
            else:
                print('You need to pick one of the numbers above')
        except ValueError:
            print('You need to enter a correct value')
            input_is_correct = False
        except Exception as e:
            print(f'There is an error {str(e)}')
            input_is_correct = False

    return choice

# writing list items to files 
def write_to_file(filepath, items, to_json = False):
    try:
        with open(filepath, 'w') as file:
            keys = items[0].keys()
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(items)
    except Exception as e:
            print(f'There is an error {str(e)}')

# reading files and populate list items            
def read_from_file(filepath):
    try:
        file_items = []
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for line in reader:
                file_items.append(line)
        return file_items
    except FileNotFoundError as fnfe:
        print(f'Your file was not found')
        return []

def create_product_id():
    return shortuuid.uuid()[:7]

def create_courier_id():
    return shortuuid.uuid()[:6]

# add item to items, name is either product or courier (str) and items is a list
def add_product(db_helper: DBHelper):
    product_name = str(input(f'\nPlease enter the name of the product: '))
    price = float(input(f'\nPlease enter the price of the new product: '))
    
    sql = f'INSERT INTO product(ProductName, Price) VALUES ("{product_name}", "{price}")'
    db_helper.execute(sql)

    print(f'{product_name} with a price of {price} has been added to the menu!\n')

def add_courier(db_helper: DBHelper):
    first_name = str(input(f'\nPlease enter the first name: '))
    last_name = str(input(f'\nPlease enter the last name: '))
    phone_number = input(f'\nPlease enter the phone number: ')
    
    sql = f'INSERT INTO courier(FirstName, LastName, PhoneNumber) VALUES ("{first_name}", "{last_name}", "{phone_number}")'
    
    try:
        db_helper.execute(sql)
        print(f'{first_name} {last_name} with a phone number of {phone_number} has been added to the couriers\n')
    except Exception as e:
        print(f'There was an error {e}')

def show_items(item_name: str, table_name: str, db_helper: DBHelper):
    print(f'Here\'s a list of the {item_name}s\n')
    
    sql = f'SELECT * FROM {table_name}'
    items = db_helper.fetch(sql)
    
    for index, item in enumerate(items, 1):
        print(f'[{index}] - {item}')

    return items

def show_all_orders(table1: str, table2: str, db_helper: DBHelper):
    orders = show_items('order', 'order_info', db_helper)
    order_id = ''
    
    correct_input = False
    while correct_input == False:
        order_id = input('If you would like to see the products in each other please enter the Order ID here'
                         '\nOtherwise leave blank and hit enter to return to the main menu: ')
        
        if order_id.strip() == '':
            return
        
        # see if the order id matches any of the order ids in the orders list
        for order in orders:
            if order["OrderID"] == order_id:
                correct_input = True
        
        # leave the while loop if order id is correct              
        if correct_input:
            break
        
        print('You have not entered a correct Order ID')
    
    show_order_products(order_id, db_helper)
    print('Show order products should have ran')
    # sql = f'SELECT * FROM order_product WHERE OrderID="{order_id}"'
    # orders = db_helper.fetch(sql)
    
    # for index, order in enumerate(orders, 1):
    #     print(f'[{index}] - {order}')

    # return orders

def show_order_products(order_id: str, db_helper: DBHelper):
    sql = f'''SELECT order_product.OrderID, product.ProductID, product.ProductName, order_product.Quantity, product.Price
        FROM order_product
        INNER JOIN product ON order_product.ProductID=product.ProductID
        WHERE order_product.OrderID="{order_id}"
    '''
    order = db_helper.fetch(sql)
    print(f'order: {order}')
    for item in order:
        print(item)
    
def show_orders_by_status(db_helper: DBHelper):
    sql = f'''SELECT order_info.OrderID, status.Status
        FROM order_info
        INNER JOIN status ON order_info.StatusID=status.StatusID
    '''
    orders = db_helper.fetch(sql)
    
    for index, order in enumerate(orders, 1):
        print(f'[{index}] - {order}')

    return orders

def show_orders_by_courier(db_helper: DBHelper):
    sql = f'''SELECT order_info.OrderID, courier.CourierID, CONCAT_WS(" ", courier.Firstname, courier.Lastname) AS FullName
        FROM order_info
        INNER JOIN courier ON order_info.CourierID=courier.CourierID
    '''
    orders = db_helper.fetch(sql)
    
    for index, order in enumerate(orders, 1):
        print(f'[{index}] - {order}')

    return orders
                     
# remove an existing item from items list
def remove_item(name: str, table: str, db_helper: DBHelper):
    items = show_items(name, table, db_helper)
    id_field_name = f'{name.capitalize()}ID'
    selected_id = ''
        
    correct_input = False
    while correct_input == False:
        selected_id = input(f'Please enter the {id_field_name} of the {name} ' 
                            'you would like removed or enter "q" to return to the main ' 
                            'menu: ')
        
        for item in items:
            if item.get(id_field_name) == selected_id:
                correct_input = True
        
        if selected_id == 'q':
            return
        elif correct_input == True:
            continue
        else:    
            print(f'You entered an incorrect {id_field_name}')
    
    if name == 'order':
        try:
            sql = f'DELETE FROM order_product WHERE {id_field_name} = "{selected_id}"'
            db_helper.execute(sql)
            sql = f'DELETE FROM {table} WHERE {id_field_name} = "{selected_id}"'
            db_helper.execute(sql)
        except Exception as e:
            print(f'Something went wrong {e}')
    else:    
        try:
            sql = f'DELETE FROM {table} WHERE {id_field_name} = "{selected_id}"'
            db_helper.execute(sql)
        except Exception as e:
            print(f'Something went wrong {e}')
    
    print(f'Here is the updated list of {name}s:')
    show_items(name, table, db_helper)

def create_order_id():
    return shortuuid.uuid()[:7]

def choose_courier(db_helper: DBHelper):
    couriers = show_items('courier', 'courier', db_helper)
    courier_id = None
    
    correct_input = False
    while correct_input == False:
        
        try:
            courier_id = int(input('Please select the courier id you want to deliver this order: '))

            for courier in couriers:
                if courier["CourierID"] == courier_id:
                    return courier_id

            print('You must enter a correct courier id. Try again')
            
        except Exception:
            print('You must enter a number')
    
    return courier_id

def choose_products(order_id, db_helper):
    products = show_items('product', 'product', db_helper)
    order = []

    correct_input = False
    while correct_input == False:
        product_id = None
        quantity = None
        correct_product_id = False
        
        try:
            product_id = int(input('Please enter the product id you want to add to your order: '))
            
            for product in products:
                if product["ProductID"] == product_id:
                    correct_product_id = True
            
            if correct_product_id == False:
                print('You need to enter a correct product id')
                continue
            
        except Exception:
            print('You must enter a number')
            continue
        
        try:
            quantity = int(input('Please enter the quantity you want: '))
        except Exception:
            print('You must enter a number')
        
        order.append((order_id, product_id, quantity))
        
        finished_selection = input('Would you like to add another product to your order?\n"n" to exit or hit enter to add more products: ')
        
        if finished_selection == 'n':
            correct_input = True
        else:
            continue
            
    return order

def choose_status(db_helper: DBHelper):
    all_status = show_items('status', 'status', db_helper)
    status_id = None
    
    correct_input = False
    while correct_input == False:
        
        try:
            status_id = int(input('Please select the status id you want to deliver this order'))

            for status in all_status:
                if status["StatusID"] == status_id:
                    return status_id

            print('You must enter a correct status id. Try again')
            
        except Exception:
            print('You must enter a number')
    
    return status_id
            
def add_order(db_helper: DBHelper):
    print(f'Please enter the details of your order')
    
    # # Getting customer information to an entry in the customer table
    customer = Customer.get_user_input()
    customer_sql = f'INSERT INTO customer(FirstName, LastName, PhoneNumber, Address, Email) VALUES ("{customer.first_name}", "{customer.last_name}", "{customer.phone_number}", "{customer.address}", "{customer.email}");\n'

    # # db_helper.execute(sql)
    
    # # info to create an entry in the order table
    order_id = create_order_id()
    customer_id = customer.email
    courier_id = choose_courier(db_helper)
    status_id = choose_status(db_helper)
    order_info_sql = f'INSERT INTO order_info(OrderID, CustomerID, CourierID, StatusID) VALUES ("{order_id}", "{customer_id}", "{courier_id}", "{status_id}");\n'
    
    # getting products
    products = choose_products(order_id, db_helper)
    order_product_sql = 'INSERT INTO order_product (OrderID, ProductID, Quantity) VALUES (%s, %s, %s);\n'

    #execute SQL statements after collecting info
    db_helper.execute(customer_sql)
    db_helper.execute(order_info_sql)
    db_helper.execute_many(order_product_sql, products)

def update_order(db_helper: DBHelper):
    orders = show_items('order', 'order_info', db_helper)
    selected_order = dict()
    
    correct_input = False
    while correct_input == False:
        
        try:    
            order_index = input('Please enter the index of the order you would like to update\n'
                                'Or leave blank to return to the main menu: ')
            
            if order_index.strip() == '': return
            
            order_index = int(order_index) - 1 # decrease 1 as index starts from 0 but our enumerate starts at 1
        except Exception as e:
            print('You must enter a number')
            continue
        
        if order_index >= 1 and order_index <= len(orders):
            # - 1 as index starts from 0 but our enumerate starts at 1
            order_index -= 1
            correct_input = True
            selected_order = orders[order_index]
            print(f'You have selected {selected_order["OrderID"]}')
        
    selected_order["CourierID"] = choose_courier(db_helper)
    selected_order["StatusID"] = choose_status(db_helper)
    
    sql = f'UPDATE order_info SET CourierID={selected_order["CourierID"]}, StatusID={selected_order["StatusID"]} WHERE OrderID="{selected_order["OrderID"]}"'
    print(f'Updating your courier to {selected_order["CourierID"]} and status to {selected_order["StatusID"]}')
    db_helper.execute(sql)

def update_product(db_helper: DBHelper):
    products = show_items('product', 'product', db_helper)
    selected_product = dict()
    new_product_name = None
    new_product_price = None
    
    correct_input = False
    while correct_input == False:
        
        try:    
            product_index = input('Please enter the index of the product you would like to update\n'
                                'Or leave blank to return to the main menu: ')
            
            if product_index.strip() == '': return
            
            product_index = int(product_index) 
        except Exception as e:
            print('You must enter a number')
            continue
        
        print(f'product index value {product_index}')
        if product_index >= 1 and product_index <= len(products):
            # - 1 as index starts from 0 but our enumerate starts at 1
            product_index -= 1
            correct_input = True
            selected_product = products[product_index]
            print(f'You have selected {selected_product["ProductName"]}')
            
    correct_input = False
    while correct_input == False:    
        new_product_name = input('Enter a new product name: ')
        
        try:
            new_product_price = float(input('Enter a new product price: '))
            if len(new_product_name) > 0 and new_product_price > 0:
                correct_input = True
        except Exception:
            print('You need to enter a valid number for the new price')
    
    selected_product["ProductName"] = new_product_name
    selected_product["Price"] = new_product_price
    
    sql = f'''UPDATE product 
        SET ProductName="{selected_product["ProductName"]}", Price={selected_product["Price"]} 
        WHERE ProductID={selected_product["ProductID"]}'''
    db_helper.execute(sql)

    print(f'Updated the name to {selected_product["ProductName"]} and price to {selected_product["Price"]}')

def update_courier(db_helper: DBHelper):
    couriers = show_items('courier', 'courier', db_helper)
    selected_courier = dict()
    new_courier_first_name = None
    new_courier_last_name = None
    new_courier_price = None
    
    correct_input = False
    while correct_input == False:
        
        try:    
            courier_index = input('Please enter the index of the courier you would like to update\n'
                                'Or leave blank to return to the main menu: ')
            
            if courier_index.strip() == '': return
            
            courier_index = int(courier_index) 
        except Exception as e:
            print('You must enter a number')
            continue
        
        print(f'courier index value {courier_index}')
        if courier_index >= 1 and courier_index <= len(couriers):
            # - 1 as index starts from 0 but our enumerate starts at 1
            courier_index -= 1
            correct_input = True
            selected_courier = couriers[courier_index]
            print(f'You have selected {selected_courier["FirstName"]} {selected_courier["LastName"]}')
            
    correct_input = False
    while correct_input == False:    
        new_courier_first_name = input('Enter a new first name: ')
        new_courier_last_name = input('Enter a new last name: ')
        new_courier_phone_number = input('Enter a new phone number: ')
        
        if (len(new_courier_first_name) > 0 and len(new_courier_last_name) > 0 and len(new_courier_phone_number) > 0):
            correct_input = True
    
    selected_courier["FirstName"] = new_courier_first_name
    selected_courier["LastName"] = new_courier_last_name
    selected_courier["PhoneNumber"] = new_courier_phone_number
    
    sql = f'''UPDATE courier 
        SET FirstName="{selected_courier["FirstName"]}", 
        LastName="{selected_courier["LastName"]}", 
        PhoneNumber="{selected_courier["PhoneNumber"]}"
        WHERE CourierID="{selected_courier["CourierID"]}"
        '''
        
    db_helper.execute(sql)

    print(f'Updated the name to {selected_courier["FirstName"]} {selected_courier["LastName"]} and phone number to {selected_courier["PhoneNumber"]}')
    
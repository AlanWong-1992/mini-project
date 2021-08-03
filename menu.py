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
    
    # product = {
    #     'name': product_name,
    #     'price': price
    # }
    
    sql = f'INSERT INTO product(ProductName, Price) VALUES ("{product_name}", "{price}")'
    db_helper.execute(sql)
    
    # print(sql)
    # products.append(product)
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

def show_items(item_type: str, db_helper: DBHelper):
    print(f'Here\'s a list of the {item_type}s\n')
    
    sql = f'SELECT * FROM {item_type}'
    items = db_helper.fetch(sql)
    
    for index, item in enumerate(items, 1):
        print(f'[{index}] - {item}')

    return items

def show_orders_by_status(orders: List[Dict]):
    orders_by_status = []
    status = choose_status()
    
    for index, order in enumerate(orders):
        if(status) == order['status']:
            orders_by_status.append(order)
    
    print('These are your orders by status')
    
    for index, order in enumerate(orders_by_status):
        if(status) == order['status']:
            print(f'[{index}] - {order}')

def show_orders_by_courier(orders: List[Dict], couriers: List[Dict]):
    orders_by_courier = []
    courier_index = choose_courier(couriers)
    
    for order in orders:
        if(courier_index) == order['courier']:
            orders_by_courier.append(order)
    
    print('These are your orders by courier')
    
    for index, order in enumerate(orders_by_courier):
        print(f'[{index}] - {order}')
                     
# remove an existing item from items list
def remove_item(item_type, db_helper):
    show_items(item_type, db_helper)
    
    id_field_name = f'{item_type.capitalize()}ID'
    
    selected_id = input('Please enter the {id_field_name} of the {item_type}' 
                        'you would like removed or enter "q" to return to the main'
                        'menu')
    
    try:
        sql = f'DELETE FROM {item_type} WHERE {id_field_name} = "{selected_id}"'
        db_helper.execute(sql)
    except Exception as e:
        print(f'Something went wrong {e}')
    
    print(f'Here is the updated list of {item_type}s:')
    show_items(item_type, db_helper)

def create_order_id():
    return shortuuid.uuid()[:7]

def choose_courier(db_helper: DBHelper):
    couriers = show_items('courier', db_helper)
    courier_id = None
    
    correct_input = False
    while correct_input == False:
        
        try:
            courier_id = int(input('Please select the courier id you want to deliver this order'))

            for courier in couriers:
                if courier["CourierID"] == courier_id:
                    return courier_id

            print('You must enter a correct courier id. Try again')
            
        except Exception:
            print('You must enter a number')
    
    return courier_id
    # if len(couriers) < 1: return 'You need to employ or add some couriers!'
    # show_items('courier', couriers)
    
    # correct_index = False
    
    # while correct_index == False:
    #     index = input('Please choose a courier')
        
    #     try:
    #         index = int(index)
    #         if index >=0 and index <= len(couriers) - 1:
    #             correct_index = True
    #             print(f'your index is {index}') #and the couriers[{index}] is: {couriers[index]} and the id value is: {couriers[index]["id"]}')
    #             print(f'couriers item: {couriers[index]}')
    #             print(f'couriers id: {couriers[index].get("id")}')
    #             return couriers[index]['id']
    #         else:
    #             print('Please enter a valid index from the options above')
    #     except Exception as e:
    #         print(f'Please enter a valid value the error is {e}')

def choose_products(order_id, db_helper):
    products = show_items('product', db_helper)
    order = []

    correct_input = False
    while correct_input == False:
        product_id = None
        quantity = None
        correct_product_id = False
        
        try:
            product_id = int(input('Please enter the product id you want to add to your order'))
            
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
            quantity = int(input('Please enter the quantity you want'))
        except Exception:
            print('You must enter a number')
        
        order.append((order_id, product_id, quantity))
        
        finished_selection = input('Would you like to add another product to your order? [y/n]')
        
        if finished_selection == 'n':
            correct_input = True
        else:
            continue
            
    return order
    
    # num_of_products = len(products)
    # order_basket = []

    # finished_selecting = False
    # while finished_selecting == False:
    #     show_items('product', products)
    #     product_index = input('Please choose from the list above or type in "f" to finish order selection: ')
        
    #     if product_index == 'f' and len(order_basket) > 0: 
    #         finished_selecting = True
    #         return order_basket
    #     elif product_index == 'f' and len(order_basket) == 0:
    #         print('You need to have at least 1 item in your order')
    #         continue 
        
    #     try:
    #         product_index = int(product_index)
    #         quantity = int(input('How many would you like? '))
    #         if product_index >= 0 and product_index <= num_of_products - 1:
    #             order_basket.extend(repeat(products[product_index]['id'], quantity))
    #         else:
    #             print('You need to enter a correct product option and entries must be numbers')
                
    #     except Exception as e:
    #         print(f'Please enter a valid value the error is {e}')

def choose_status(db_helper: DBHelper):
    all_status = show_items('status', db_helper)
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

    # possible_status = ['Preparing', 'Out for delivery', 'Delivered']
    # for index, value in enumerate(possible_status):
    #     print(f'[{index + 1}] - {value}')
    
    # correct_input = False
    # while correct_input == False:
    #     selected_status = input('Please pick a status for your order\n')
    #     try:
    #         selected_status = int(selected_status)
    #         if selected_status >= 1 and selected_status <= len(possible_status):
    #             return possible_status[selected_status - 1]
    #         else:
    #             print('You need to enter a valid option')
    #     except Exception as e:
    #         print(f'Please enter a valid value')
            
            
def add_order(db_helper: DBHelper):
    print(f'Please enter the details of your order')
    
    # customer details
    # first_name = input('What is the first name? ')
    # last_name = input('What is the last name? ')
    # phone_number = input('What is the phone number? ')
    # address = input('What is the address? ')
    # email = input('What is the email address? ')
    
    # # Getting customer information to an entry in the customer table
    customer = Customer.get_user_input()
    customer_sql = f'INSERT INTO customer(FirstName, LastName, PhoneNumber, Address, Email) VALUES ("{customer.first_name}", "{customer.last_name}", "{customer.phone_number}", "{customer.address}", "{customer.email}")'

    # # db_helper.execute(sql)
    
    # # info to create an entry in the order table
    order_id = create_order_id()
    customer_id = customer.email
    courier_id = choose_courier(db_helper)
    status_id = choose_status(db_helper)
    order_info_sql = f'INSERT INTO order_info(OrderID, CustomerID, CourierID, StatusID) VALUES ("{order_id}", "{customer_id}", "{courier_id}", "{status_id}")'
    
    # getting products
    products = choose_products(order_id, db_helper)
    order_product_sql = 'INSERT INTO order_product (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)'

    # order_product_sql = 'INSERT INTO test (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)'

    print(products)
    #execute SQL statements after collecting info
    db_helper.execute(customer_sql)
    db_helper.execute(order_info_sql)
    db_helper.execute_many(order_product_sql, products)
    
    # print(f'This is your order at the moment {order_basket}')
    
    
    
    # order = {
    #     'order_id': order_id,
    #     'customer_name': customer_name,
    #     'customer_address': customer_address,
    #     'customer_phone_number': customer_phone_number,
    #     'courier': courier_id,
    #     'products': order_basket,
    #     'status': status
    # }
    
    # orders.append(order)

def update_item(name, items: List[Dict], products: List[Dict] = None, couriers: List[Dict] = None):
    # loop to choose an order to change
    change_order = True
    while change_order:
        num_of_items = len(items)
        # show user the list of items they can update
        show_items(name, items)
        item_index = item_to_change(num_of_items)
        
        if(item_index == 'q'): 
            change_order = False
            break
        
        selected_item = items[item_index]
        
        selected_field = select_field_to_change(selected_item)
        
        if (selected_field) == False: break
        
        update_item_field(name, selected_field, selected_item, products, couriers)

def item_to_change(num_orders: int):
    correct_input = False
    while correct_input == False:
        index = input('Choose the index of the item you want to change or "q" to return to main menu: ')
    
        if(index == 'q'): return 'q'
        
        try:
            index = int(index)
            if(index >= 0 and index <= num_orders - 1):
                correct_input = True
                return index
            else:
                print('You need to enter a valid number')
        except ValueError as ve:
            print('You need to enter a correct value')
            
def select_field_to_change(item):
    correct_input = False
    while correct_input == False:
        field_options_message = ''
        num_options = len(item) - 1
        field_options = []
        
        for count, key in enumerate(item):
            
            field_options.append((count, key))
            
            # skipping 0 as this is the id for the products, couriers, and orders 
            # which the user shouldn't change but we want for our field options 
            # list to easier select the key later in the function
            if count == 0: continue 
            
            field_options_message += f'{count} - {key}\n'
            
        index = input(f'What would you like to update?\n{field_options_message}')

        try:
            index = int(index)
            if(index >= 1 and index <= num_options):
                correct_input = True
                return field_options[index][1]
            else:
                print(f'You need to enter a number from 1 - {num_options}')
        except ValueError as ve:
            print('You need to enter a valid number')

def update_item_field(name: str, item_key: str, item: Dict, products: List[Dict] = None, couriers: List[Dict]=None):
    #if-else block just for updating orders
    if (name == 'order' and item_key == 'courier'):
        courier_id = choose_courier(couriers)
        item[item_key] = courier_id
        return
    elif (name == 'order' and item_key == 'products'):
        order_basket = choose_products(products)
        item[item_key] = order_basket
        return
    elif (name == 'order' and item_key == 'status'):
        status = choose_status()
        item[item_key] = status
        return
    
    new_value = input(f'Please enter the new {item_key}: ')
    item[item_key] = new_value


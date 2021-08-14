import csv
import shortuuid
from typing import List, Dict
from itertools import repeat
from db_helper import DBHelper
from product import Product
from courier import Courier
# from order import Order
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

# def write_to_file(filepath, items, to_json = False):
#     try:
#         with open(filepath, 'w') as file:
#             keys = items[0].keys()
#             writer = csv.DictWriter(file, keys)
#             writer.writeheader()
#             writer.writerows(items)
#     except Exception as e:
#             print(f'There is an error {str(e)}')

def write_to_file(filepath, items, to_json = False):
    try:
        with open(filepath, 'w') as file:
            keys = vars(items[0]).keys()
            writer = csv.writer(file)
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            for item in items:
                writer.writerow(vars(item))
    except Exception as e:
            print(f'There is an error {str(e)}')

# reading files and populate list items            
def read_from_file(name: str, filepath: str):
    try:
        file_items = []
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                
                if name == 'products':
                    print(f'line 0 is {line[0]}, line 1 is {line[1]}, line 2 is {line[2]}, line 3 is {line[3]}')
                    file_items.append(Product(line[0], line[1], line[2], line[3]))
                elif name == 'couriers':
                    print('Creating a courier object...')
                    file_items.append(Courier(line[0], line[1], line[2], line[3], line[4]))
                # elif name == 'orders':
                #     file_items.append(Order(line[0], line[1], line[2], line[3]))
                elif name == 'customers':
                    file_items.append(Customer(line[0], line[1], line[2], line[3], line[4], line[5]))
        return file_items
    except FileNotFoundError as fnfe:
        print(f'Your file was not found')
        return []
    except Exception as e:
        print(f'There was an error {e}. Returning an empty list')
        return []
    
def create_product_id():
    return shortuuid.uuid()[:7]

def create_courier_id():
    return shortuuid.uuid()[:6]

# add item to items, name is either product or courier (str) and items is a list
def add_product(products):
    name = str(input(f'\nPlease enter a new product name: '))
    price = float(input(f'\nPlease enter the price of the new product: '))
    
    product = {
        'id': create_product_id(),
        'name': name,
        'price': price
    }
    
    products.append(product)
    print(f'Updated products: {products}')

def add_courier(couriers):
    name = str(input(f'\nPlease enter a name: '))
    phone_number = input(f'\nPlease enter a phone number: ')
    
    courier = {
        'id': create_courier_id(),
        'courier_name': name,
        'phone_number': phone_number
    }
    
    couriers.append(courier)
    print(f'Updated courierss: {couriers}')

def show_items(name: str, items: List[Dict]):
    print(f'Here\'s a list of the {name}s\n')
    for index, item in enumerate(items):
        print(f'[{index}] - {item}')

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
def remove_item(name, items):
    show_items(name, items)
    
    index = -1
    while index < 0 or index > len(items) - 1:
        try: 
            index = int(input('Choose the index of the item you want to delete (Must be a valid index number): '))
        except ValueError:
            print('You need to enter a valid number')
        except Exception as e:
            print(f'You have an error: {str(e)}')
            
    items.pop(index)
    
    print(f'Here is the updated list of {name}s:')
    show_items(name, items)

def create_order_id():
    return shortuuid.uuid()

def choose_courier(couriers: List[Dict]):
    if len(couriers) < 1: return 'You need to employ or add some couriers!'
    show_items('courier', couriers)
    
    correct_index = False
    
    while correct_index == False:
        index = input('Please choose a courier')
        
        try:
            index = int(index)
            if index >=0 and index <= len(couriers) - 1:
                correct_index = True
                print(f'your index is {index}') #and the couriers[{index}] is: {couriers[index]} and the id value is: {couriers[index]["id"]}')
                print(f'couriers item: {couriers[index]}')
                print(f'couriers id: {couriers[index].get("id")}')
                return couriers[index]['id']
            else:
                print('Please enter a valid index from the options above')
        except Exception as e:
            print(f'Please enter a valid value the error is {e}')

def choose_products(products: List[Dict]):
    num_of_products = len(products)
    order_basket = []

    finished_selecting = False
    while finished_selecting == False:
        show_items('product', products)
        product_index = input('Please choose from the list above or type in "f" to finish order selection: ')
        
        if product_index == 'f' and len(order_basket) > 0: 
            finished_selecting = True
            return order_basket
        elif product_index == 'f' and len(order_basket) == 0:
            print('You need to have at least 1 item in your order')
            continue 
        
        try:
            product_index = int(product_index)
            quantity = int(input('How many would you like? '))
            if product_index >= 0 and product_index <= num_of_products - 1:
                order_basket.extend(repeat(products[product_index]['id'], quantity))
            else:
                print('You need to enter a correct product option and entries must be numbers')
                
        except Exception as e:
            print(f'Please enter a valid value the error is {e}')

def choose_status():
    possible_status = ['Preparing', 'Out for delivery', 'Delivered']
    for index, value in enumerate(possible_status):
        print(f'[{index + 1}] - {value}')
    
    correct_input = False
    while correct_input == False:
        selected_status = input('Please pick a status for your order\n')
        try:
            selected_status = int(selected_status)
            if selected_status >= 1 and selected_status <= len(possible_status):
                return possible_status[selected_status - 1]
            else:
                print('You need to enter a valid option')
        except Exception as e:
            print(f'Please enter a valid value')
    
        
def add_order(products: List[Dict], couriers: List[Dict], orders: List[Dict], create_order_id):
    print(f'Please enter the details of your order')
    order_id = create_order_id()
    customer_name = input('What is your full name? ')
    customer_address = input('What is your address? ')
    customer_phone_number = input('What is your phone number? ')
    courier_id = choose_courier(couriers)
    order_basket = choose_products(products)
    status = choose_status()
    
    order = {
        'order_id': order_id,
        'customer_name': customer_name,
        'customer_address': customer_address,
        'customer_phone_number': customer_phone_number,
        'courier': courier_id,
        'products': order_basket,
        'status': status
    }
    
    orders.append(order)

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
    
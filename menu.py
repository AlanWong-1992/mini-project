import json
import random
import shortuuid
from typing import List, Dict

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
            if (type(choice) == int and choice <=3 and choice >=0):
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

# writing list items to files 
def write_to_file(file, items, to_json = False):
    # if to_json if false then we want to save each item in items in a txt file
    # else if to_json is true we want to save in a json file as each item in items will be a Dict
    if (to_json == False):
        try:
            with open(file, 'w') as fh:
                for item in items:
                    fh.write(f'{item}\n')
        except Exception as e:
                print(f'There is an error {str(e)}')
    elif (to_json == True):
        try:
            with open(file, 'w') as fh:
                json.dump(items, fh, indent=4)
        except Exception as e:
            print(f'There is an error {str(e)}')
    else:
        print('You need to enter a correct json value')    

# reading files and populate list items            
def read_from_file(file, to_json = False):
    # if to_json if false then we will read from a txt file
    # else if to_json is true we will read from a json file
    if (to_json == False):
        try:
            with open(file, 'r') as fh:
                all_lines = fh.readlines()
                items = []
                for line in all_lines:
                    if(line != '\n'): 
                        items.append(line.rstrip())
                return items        
        except FileNotFoundError as fnfe:
                print(f'Your file was not found')
                return []
                input_is_correct = False
    elif (to_json == True):
        print('populating items using JSON')
        try:
            with open(file, 'r') as fh:
                parsed = json.load(fh)
                if(parsed is not None):
                    return parsed
                elif(parsed is None): 
                    return []
                else:
                   print('There is a problem with the application please try restarting') 
        except FileNotFoundError as fnfe:
                print(f'Your file was not found')
                return []
                input_is_correct = False
        
# add item to items, name is either product or courier (str) and items is a list
def add_item(name, items):
    item = str(input(f'\nPlease enter a new {name} name: '))
    items.append(item)
    print(f'Updated {name}s: {items}')

def show_items(name: str, items: List):
    print(f'Here\'s a list of the {name}s\n')
    for index, item in enumerate(items):
        print(f'[{index}] - {item}')
    
# update an existing item with a new name from the list by choosing an index    
def update_item(name, items):
    print(f'\nHere is a list of {name}s: {items}.\n')
    
    index = -1
    while index < 0 or index > len(items) - 1: 
        try:
            index = int(input('Choose the index of the item you want to change (first item starts at 0): '))
        except ValueError:
            print('You need to enter a valid number')
        except Exception as e:
            print(f'You have an error: {str(e)}')
            
    new_name = str(input(f'Please choose a new {name} name: '))
    items[index] = new_name
    print(f'Updated {name}s: {items}')

# remove an existing item from items list
def remove_item(name, items):
    print(f'\nHere is a list of {name}s: {items}.\n')
    
    index = -1
    while index < 0 or index > len(items) - 1:
        try: 
            index = int(input('Choose the index of the item you want to delete (Must be a valid index number): '))
        except ValueError:
            print('You need to enter a valid number')
        except Exception as e:
            print(f'You have an error: {str(e)}')
            
    items.pop(index)
    print(f'Updated {name}s: {items}')

def create_order_id():
    return shortuuid.uuid()
    
def add_order(couriers: List[str], items: List[Dict], create_order_id):
    print(f'Please enter the details of your order')
    order_id = create_order_id()
    customer_name = input('What is your full name? ')
    customer_address = input('What is your address? ')
    customer_phone_number = input('What is your phone number? ')
    courier = random.choice(couriers) if len(couriers) > 0 else 'A courier will be assigned later'
    status = 'preparing'
    
    order = {
        'order_id': order_id,
        'customer_name': customer_name,
        'customer_address': customer_address,
        'customer_phone_number': customer_phone_number,
        'courier': courier,
        'status': status
    }
    
    items.append(order)

def update_order(id: str, orders: List[Dict]):
    num_of_orders = len(orders)
    # show user the list of orders they can update
    show_items('order', orders)

    # loop to choose an order to change
    change_order = True
    while change_order:
        order_number = order_to_change(num_of_orders)
        
        if(order_number == False): break
        
        selected_field = order_field_choices()
        
        change_order_details = update_order_field(selected_field, order_number, orders)
        
        if (change_order_details) == False: break

def order_to_change(num_orders: int):
    correct_input = False
    while correct_input == False:
        index = input('Choose the index of the item you want to change or "q" to return to main menu: ')
    
        if(index == 'q'): return False
        try:
            index = int(index)
            if(index >= 0 and index <= num_orders - 1):
                correct_input = True
                return index
            else:
                print('You need to enter a number corresponding with a real order')
        except ValueError as ve:
            print('You need to enter a correct value')
            
def order_field_choices():
    correct_input = False
    while correct_input == False:
        order_field = input('\nWhat would you like to update?\n'
                            '1) The customers full name\n'
                            '2) The customers address\n'
                            '3) The customers phone number\n'
                            '4) The courier to deliver the order\n'
                            '5) The status of the order\n'
                            '6) Nothing return to main menu\n')
        try:
            order_field = int(order_field)
            if(order_field >= 1 and order_field <= 6):
                correct_input = True
                return order_field
            else:
                print('You need to enter a number from 1 - 6')
        except ValueError as ve:
            print('You need to enter a valid number')

def update_order_field(order_field: int, index: int, orders: List[Dict]):
    if (order_field >= 1 and order_field <= 6):
        if order_field == 1:
            new_order_field = input('Enter a new full name: ')
            orders[index]['customer_name'] = new_order_field
            print(f'The full name has been updated to {new_order_field}')
        if order_field == 2:
            new_order_field = input('Enter a new address: ')
            orders[index]['customer_address'] = new_order_field
            print(f'The address has been updated to {new_order_field}')
        if order_field == 3:
            new_order_field = input('Enter a new phone number: ')
            orders[index]['customer_phone_number'] = new_order_field
            print(f'The phone number has been updated to {new_order_field}')
        if order_field == 4:
            new_order_field = input('Enter a new courier: ')
            orders[index]['courier'] = new_order_field
            print(f'The courier has been updated to {new_order_field}')
        if order_field == 5:
            new_order_field = input('Enter a new status: ')
            orders[index]['status'] = new_order_field
            print(f'The order status has been updated to {new_order_field}')
        if order_field == 6:
            print(f'Returning to main menu')
            return False
    else:
        print('You need to pick a valid option')

    
    
    

import json
import random
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
        except Exception as e:
                print(f'There is an error {str(e)}')
                input_is_correct = False
    elif (to_json == True):
        print('populating items using JSON')
        try:
            with open(file, 'r') as fh:
                parsed = json.load(fh)
                if(parsed is not None):
                    return json.load(fh)
                elif(parsed is None): 
                    return []
                else:
                   print('There is a problem with the application please try restarting') 
        except Exception as e:
                print(f'There is an error {str(e)}')
                input_is_correct = False
        
# add item to items, name is either product or courier (str) and items is a list
def add_item(name, items):
    item = str(input(f'\nPlease enter a new {name} name: '))
    items.append(item)
    print(f'Updated {name}s: {items}')

def show_items(name: str, items: List):
    print(f'Here\'s a list of the {name}s\n')
    for item in items:
        print(item)
    
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
    
def add_order(couriers: List[str], items: List[Dict]):
    print(f'Please enter the details of your order')
    customer_name = input('What is your full name? ')
    customer_address = input('What is your address? ')
    customer_phone_number = input('What is your phone number? ')
    courier = random.choice(couriers)
    status = 'preparing'
    
    order = {
        'customer_name': customer_name,
        'customer_address': customer_address,
        'customer_phone_number': customer_phone_number,
        'courier': courier,
        'status': status
    }
    
    items.append(order)
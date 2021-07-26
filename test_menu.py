from unittest.mock import patch, Mock
from typing import List, Dict

def show_items(name: str, items: List):
    print(f'Here\'s a list of the {name}s\n')
    for index, item in enumerate(items):
        print(f'[{index}] - {item}')
        
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

# def test_update_order():
    #     # arrange
#     id = 'W9CPU3y4RHqUp25Bkfnn6u'
#     orders = [{"order_id": "W9CPU3y4RHqUp25Bkfnn6u", "customer_name": "David Tennant", "customer_address": "Bath", "customer_phone_number": "10291", "courier": "Ian", "status": "delivered"}]
#     expected = 

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

@patch('builtins.input', side_effects=1)
def test_order_to_change(mock_input):
    a = 5
    order_to_change(a)
    assert mock_input.call_count == 1

@patch('builtins.input', lambda *args: 3)
def test_order_to_change():
    a = 5
    expected = 3
    actual = order_to_change(a)
    
    assert actual == expected

@patch('builtins.input', lambda *args: 'q')
def test_order_to_change():
    a = 5
    expected = False
    actual = order_to_change(a)
    
    assert actual == expected

@patch('builtins.input', lambda *args: 20)
@patch('builtins.print')
def test_order_to_change(mock_print):
    a = 5
    actual = order_to_change(a)
    mock_print.assert_called_with('You need to enter a number corresponding with a real order')

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
            correct_input = True
            return order_field
        except ValueError as ve:
            print('You need to enter a valid number')

@patch()
def test_order_field_choices():
    

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
            
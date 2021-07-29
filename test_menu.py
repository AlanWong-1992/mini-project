from unittest.mock import patch, Mock
from typing import List, Dict

def show_items(name: str, items: List):
    print(f'Here\'s a list of the {name}s\n')
    for index, item in enumerate(items):
        print(f'[{index}] - {item}')
        
def update_order(orders: List[Dict], show_items, order_to_change, order_field_choices, update_order_field):
    num_of_orders = len(orders)
    # show user the list of orders they can update
    show_items('order', orders)

    # loop to choose an order to change
    change_order = True
    while change_order:
        order_number = order_to_change(num_of_orders)
        
        if(order_number == 'q'): break
        
        selected_field = order_field_choices()
        
        change_order_details = update_order_field(selected_field, order_number, orders)
        
        if (change_order_details) == False: break

def test_update_order():

    id = 'W9CPU3y4RHqUp25Bkfnn6u'
    orders = [{"order_id": "W9CPU3y4RHqUp25Bkfnn6u", "customer_name": "David Tennant", "customer_address": "Bath", "customer_phone_number": "10291", "courier": "Ian", "status": "delivered"}]
    
    mock_show_items = Mock()
    mock_order_to_change = Mock()
    mock_order_field_choices = Mock()
    mock_update_order_field = Mock()
    
    mock_show_items.return_value = False
    mock_order_to_change.return_value = 0
    mock_order_field_choices.return_value = 1
    mock_update_order_field.return_value = False
    
    actual = update_order(orders, mock_show_items, mock_order_to_change, mock_order_field_choices, mock_update_order_field)
    assert mock_show_items.assert_called_once
    assert mock_order_to_change.assert_called_once
    assert mock_order_field_choices.assert_called_once
    assert mock_update_order_field.assert_called_once
    
def order_to_change(num_orders: int):
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

def get_user_details():    
    name = input('Please enter your name: ')    
    age = int(input('Please enter your age: '))    
    print(f'Thank you, your name is {name} and your age is {age}')
    
@patch('builtins.input', side_effect=['Jane', '25'])
@patch('builtins.print')
def test_get_user_details(mock_print, mock_input):    
    get_user_details()    
    mock_print.assert_called_with("Thank you, your name is Jane and your age is 25")    
    assert mock_input.call_count == 2    
    assert mock_print.call_count == 1
    
@patch('builtins.input', side_effect=[10, 20, 30, 4])
def test_order_to_change(mock_input):
    a = 5
    order_to_change(a)
    assert mock_input.call_count == 4

@patch('builtins.input', side_effect = [20, 1])
@patch('builtins.print')
def test_order_to_change(mock_print, mock_input):
    a = 5
    order_to_change(a)
    mock_print.assert_called_with('You need to enter a number corresponding with a real order')
    assert mock_input.call_count == 2

@patch('builtins.input', side_effect = [20, 1])
@patch('builtins.print')
def test_order_to_change(mock_print, mock_input):
    a = 5
    order_to_change(a)
    mock_print.assert_called_with('You need to enter a number corresponding with a real order')
    assert mock_input.call_count == 2    
    
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

@patch('builtins.input', side_effect=[1])
def test_order_field_choices(mock_input):
    expected = 1
    actual = order_field_choices()
    
    assert actual == expected
    assert mock_input.call_count == 1

@patch('builtins.input', side_effect = [20, 1])
@patch('builtins.print')
def test_order_field_choices(mock_print, mock_input):

    expected = 1
    actual = order_field_choices()
    mock_print.assert_called_with('You need to enter a number from 1 - 6')
    assert expected == actual
    assert mock_input.call_count == 2    
    
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

@patch('builtins.input', side_effect=['Mel Gibson'])
@patch('builtins.print')
def test_update_order_field(mock_print, mock_input):
    order_field = 1
    index = 0
    orders = [{"order_id": "W9CPU3y4RHqUp25Bkfnn6u", "customer_name": "David Tennant", "customer_address": "Bath", "customer_phone_number": "10291", "courier": "Ian", "status": "delivered"}]
    expected = 'Mel Gibson'
    
    update_order_field(order_field, index, orders)
    actual = orders[0]['customer_name']
    
    mock_print.assert_called_with('The full name has been updated to Mel Gibson')
    assert mock_input.called_once
    assert actual == expected

@patch('builtins.print')
def test_update_order_field(mock_print):
    order_field = 100
    index = 0
    orders = [{"order_id": "W9CPU3y4RHqUp25Bkfnn6u", "customer_name": "David Tennant", "customer_address": "Bath", "customer_phone_number": "10291", "courier": "Ian", "status": "delivered"}]
    
    update_order_field(order_field, index, orders)
    
    mock_print.assert_called_with('You need to pick a valid option')
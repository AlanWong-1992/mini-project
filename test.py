from typing import List, Dict

list_dicts = [{
    'person_id': 'Ojdo10',
    'first_name': 'alan',
    'last_name': 'wong',
    'age': 29,
    'hair_color': 'black'
}]

order = {
    'order_id': 2121931,
    'customer_name': 'Ben Hope',
    'customer_address': 'London',
    'customer_phone_number': '079',
    'courier': 'Jamal',
    'status': 'PREPARING'
}

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
        
selected_field = select_field_to_change(list_dicts[0])
# print('selected field is: ' + selected_field)

def update_item_field(item_key: str, item_index: int, items: List[Dict]):
    item = items[item_index]
    new_value = input(f'Please enter the new {item_key}: ')
    item[item_key] = new_value

update_item_field(selected_field, 0, list_dicts)      


   
    # if (field_choice >= 1 and field_choice <= 6):
    #     if field_choice == 1:
    #         new_field_choice = input('Enter a new full name: ')
    #         items[item_index]['customer_name'] = new_field_choice
    #         print(f'The full name has been updated to {new_field_choice}')
    #     if field_choice == 2:
    #         new_field_choice = input('Enter a new address: ')
    #         items[item_index]['customer_address'] = new_field_choice
    #         print(f'The address has been updated to {new_field_choice}')
    #     if field_choice == 3:
    #         new_field_choice = input('Enter a new phone number: ')
    #         items[item_index]['customer_phone_number'] = new_field_choice
    #         print(f'The phone number has been updated to {new_field_choice}')
    #     if field_choice == 4:
    #         new_field_choice = input('Enter a new courier: ')
    #         items[item_index]['courier'] = new_field_choice
    #         print(f'The courier has been updated to {new_field_choice}')
    #     if field_choice == 5:
    #         new_field_choice = input('Enter a new status: ')
    #         items[item_index]['status'] = new_field_choice
    #         print(f'The order status has been updated to {new_field_choice}')
    #     if field_choice == 6:
    #         print(f'Returning to main menu')
    #         return False
    # else:
    #     print('You need to pick a valid option')
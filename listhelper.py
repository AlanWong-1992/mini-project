from typing import List, Dict, Union
from customer import Customer
from product import Product
from courier import Courier

class ListHelper:
    
    # def __init__(self, products, couriers, orders, customers):
    #     self.products = products
    #     self.couriers = couriers
    #     self.orders = orders
    #     self.customers = customers

    def add_item(self, item: Union[Customer, Product, Courier], items: List[Union[Customer, Product, Courier]]):
        items.append(item)
        
        print('Here is your new up-to-date list: ')
        self.show_items(items)
        
    def update_item(self, item: Union[Customer, Product, Courier], items: List[Union[Customer, Product, Courier]]):
        pass
    
    def show_items(self, items: List[Union[Customer, Product, Courier]]):
        for index, item in enumerate(items, 1):
            print(f'[{index}] - {item}')
    
    def delete_item(self, items: List[Union[Customer, Product, Courier]]):
        self.show_items(items)
    
        index = -1
        while index < 1 or index > len(items):
            try: 
                index = int(input('Choose the index of the item you want to delete (Must be a valid index number): '))
            except ValueError:
                print('You need to enter a valid number')
            except Exception as e:
                print(f'You have an error: {str(e)}')
    
        items.pop(index - 1) # reduce by 1 to account for 0 index for lists
        
        print(f'Here is the updated list:')
        self.show_items(items)
        
    def update_item(self, items: List[Union[Customer, Product, Courier]]):
        # loop to choose an order to change
        change_order = True
        while change_order:
            num_of_items = len(items)
            
            # show user the list of items that they can update
            self.show_items(items)
            
            # user chooses the index of the item they want to change
            item_index = self._item_to_change(num_of_items)
            
            if item_index == 'q': break
            
            selected_item = items[item_index]
            
            selected_field = self._select_field_to_change(selected_item)
            
            if (selected_field) == False: break
            
            update_item_field(name, selected_field, selected_item, products, couriers)

    def _item_to_change(self, num_orders: int):
        correct_input = False
        while correct_input == False:
            index = input('Choose the index of the item you want to change or "q" to return to main menu: ')
        
            if(index == 'q'): return 'q'
            
            try:
                index = int(index)
                if(index >= 1 and index <= num_orders):
                    correct_input = True
                    # reduce by 1 as arrays are indexed from 0
                    return index - 1 
                else:
                    print('You need to enter a valid number')
            except ValueError as ve:
                print('You need to enter a correct value')
                
    def _select_field_to_change(self, item):
        correct_input = False
        while correct_input == False:
            field_options_message = ''
            # num_options = len(item) - 1
            num_options = vars(item)
            print(f'Number of options: {num_options} and the length is {len(num_options)}')
            # correct_input = True
            # field_options = []
            
            # for count, key in enumerate(item, 1):
                
            #     field_options.append((count, key))
                
            #     # skipping 0 as this is the id for the products, couriers, and orders 
            #     # which the user shouldn't change but we want for our field options 
            #     # list to easier select the key later in the function
            #     if count == 0: continue 
                
            #     field_options_message += f'{count} - {key}\n'
                
            # index = input(f'What would you like to update?\n{field_options_message}')

            # try:
            #     index = int(index)
            #     if(index >= 1 and index <= num_options):
            #         correct_input = True
            #         return field_options[index][1]
            #     else:
            #         print(f'You need to enter a number from 1 - {num_options}')
            # except ValueError as ve:
            #     print('You need to enter a valid number')

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
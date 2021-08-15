from math import prod
from typing import List, Dict, Union
from customer import Customer
from product import Product
from courier import Courier
from order import Order
from itertools import repeat

class ListHelper:
    
    # def __init__(self, products, couriers, orders, customers):
    #     self.products = products
    #     self.couriers = couriers
    #     self.orders = orders
    #     self.customers = customers

    def add_item(self, item: Union[Customer, Product, Courier], items: List[Union[Customer, Product, Courier]]):
        items.append(item)
        
        print(f'Here is your new up-to-date list of {type(item)}s: ')
        self.show_items(items)
        
    def show_items(self, items: List[Union[Customer, Product, Courier]]):
        for index, item in enumerate(items, 1):
            print(f'[{index}] - {item}')
    
    def delete_item(self, items: List[Union[Customer, Product, Courier]]):
        self.show_items(items)
        num_items = len(items)
        index = -1
        input_msg = 'Choose the index of the item you want to delete (Must be a valid index number)\nEnter "q" or leave blank to exit: '
        
        index = self._input_num_handler(input_msg, index, 1, num_items)
        
        if (index == 'q' or index == ''):
            return
        
        items.pop(index - 1) # reduce by 1 to account for 0 index for lists
        
        print(f'Here is the updated list:')
        self.show_items(items)
        
    def update_item(self, name: str, items: List[Union[Customer, Product, Courier]]):
        # loop to choose an order to change
        correct_input = False
        while correct_input == False:
            num_of_items = len(items)
            
            # show user the list of items that they can update
            self.show_items(items)
            
            # user chooses the index of the item they want to change
            item_index = self._item_to_change(num_of_items)
            
            if item_index == 'q': break
            
            selected_item = items[item_index]
            
            # item to update has been selected, keep looping to change other fields for this item
            finished_updating = False
            while finished_updating == False:
                selected_field = self._select_field_to_change(selected_item)
                
                if (selected_field == 'q' or selected_field == ''):
                    finished_updating == True
                    correct_input == True
                    break
                
                if name == 'products':
                    self._update_product(selected_field, selected_item)
                    print(f'The updated info is: {selected_item}')
                elif name == 'couriers':
                    self._update_courier(selected_field, selected_item)
                    print(f'The updated info is: {selected_item}')
                elif name == 'orders':
                    self._update_order(selected_field, selected_item)
                    print(f'The updated info is: {selected_item}')
                else:
                    print('You are leaving the update menu')
                    correct_input = True

    def _item_to_change(self, num_orders: int) -> int:
        input_msg = 'Choose the index of the item you want to change or "q" to return to main menu: '
        index = -1
        index = self._input_num_handler(input_msg, index, 1, num_orders, allow_exit=True)
    
        if index == 'q' or index == '': 
            return 'q'
        
        elif index >=1 and index <= num_orders: 
            return index - 1
                
    def _select_field_to_change(self, item) -> str:
        correct_input = False
        while correct_input == False:
            field_options_message = ''
            num_options = vars(item)
            field_options = []
            
            for count, key in enumerate(num_options, 0):
                
                field_options.append((count, key))
                
                # skipping 0 as this is the id for the products, couriers, and orders 
                # which the user shouldn't change but we want for our field options 
                # list to easier select the key later in the function
                if count == 0: continue 
                
                field_options_message += f'{count} - {key}\n'
            
            input_msg = f'What would you like to update?\n{field_options_message}Choose an option or enter "q" or leave blank to exit: '
            index = -1
            num_options = len(field_options)
            index = self._input_num_handler(input_msg, index, 1, num_options, allow_exit=True)
            
            if index == 'q' or index == '':
                return index
            
            print(f'the index is {index} and the field option of that index is {field_options[index][1]}')
            return field_options[index][1]

    def _update_product(self, product_field: str, product: Product):
        input_msg = f'Please enter the new {product_field}: '
        
        if product_field == '_name':
            new_value = input(input_msg)
            product.name = new_value
        elif product_field == '_price':
            new_value = self._is_num(input_msg, 'float')
            product.price = new_value
        elif product_field == '_quantity':
            new_value = self._is_num(input_msg, 'int')
            product.quantity = new_value
    
    def _update_courier(self, courier_field: str, courier: Courier):
        input_msg = f'Please enter the new {courier_field}: '
        
        if courier_field == '_first_name':
            new_value = input(input_msg)
            courier.first_name = new_value
        elif courier_field == '_last_name':
            new_value = input(input_msg)
            courier.last_name = new_value
        elif courier_field == '_phone_number':
            new_value = input(input_msg)
            courier.phone_number = new_value
        elif courier_field == '_email':
            new_value = input(input_msg)
            courier.email = new_value
    
    def _update_order(self, order_field: str, order: Order):
        input_msg = f'Please enter the new {order_field}: '
        
        if order_field == '_first_name':
            new_value = input(input_msg)
            order.first_name = new_value
        elif order_field == '_last_name':
            new_value = input(input_msg)
            order.last_name = new_value
        elif order_field == '_phone_number':
            new_value = input(input_msg)
            order.phone_number = new_value
        elif order_field == '_email':
            new_value = input(input_msg)
            order.email = new_value
    
    def _update_item_field(self, item_field: str, item: Union[Customer, Product, Courier]):
        #if-else block just for updating orders
        # if (name == 'order' and item_key == 'courier'):
        #     courier_id = choose_courier(couriers)
        #     item[item_key] = courier_id
        #     return
        # elif (name == 'order' and item_key == 'products'):
        #     order_basket = choose_products(products)
        #     item[item_key] = order_basket
        #     return
        # elif (name == 'order' and item_key == 'status'):
        #     status = choose_status()
        #     item[item_key] = status
        #     return
        
        new_value = input(f'Please enter the new {item_field}: ')
        item.item_field(new_value)
    
    def _is_num(self, input_msg: str, type: str) -> Union[float, int]:
        '''
        Checks if the input is a float or an int
        Used for when adding a product 
        '''
        correct_input = False
        while correct_input == False:
            value = input(input_msg)
            try:
                if type == 'float':
                    value = float(value)
                elif type == 'int':
                    value = int(value)
                    
                correct_input = True
                return value
            except ValueError as ve:
                print('You need to enter a number')
            
    def _input_num_handler(self, input_msg: str, index: int, range_low: int, range_high: int, allow_exit=False) -> int:
        '''
        Makes sure user enters numbers within a predefined range.
        allow_exit variable allows the user to enter "q" or leave blank to exit the function
        '''
        while index < range_low or index > range_high:
            index = input(input_msg)
            
            # check to see if 'q' or empty to return to main menu or leave value as is depending on the function
            if allow_exit:
                if index == 'q':
                    return 'q'
                elif index == '':
                    return ''
            
            try:
                # check to see if the right number as been entered by the user
                index = int(index)
                if(index >= range_low and index <= range_high):
                    return index
                else:
                    print(f'You need to enter a number from {range_low} - {range_high}')
            except ValueError as ve:
                print('You need to enter a valid number')
                
                # need to set index as -1 otherwise while loop will break if a non int was entered
                index = -1 
    
    def choose_courier(self, couriers: List[Courier]) -> str:
        '''
        Allows for user to select a courier based on their ID
        '''
        num_of_couriers = len(couriers)
        
        if num_of_couriers < 1: 
            print('You need to employ more couriers!')
            return
        
        self.show_items(couriers)
        
        input_msg = 'Please choose a courier: '
        index = -1
        index = self._input_num_handler(input_msg, index, 1, num_of_couriers) - 1

        return couriers[index].id
        
    def choose_products(self, products: List[Product]) -> Dict[str, int]:
        '''
        Allows user to select products for their orders. 
        Products are appended to a dictionary
        '''
        if len(products) == 0:
            print('Your shop has no products you need to add some')
            return
        
        order_basket = {}

        finished_selecting = False
        while finished_selecting == False:
            self.show_items(products)
            
            input_msg = 'Please choose from the list above or type in "q" or leave blank to finish order selection: '
            index = -1
            num_of_products = len(products)
            
            # if product index is a number we want to reduce by 1 to index list. Can return "q" or blank as well
            product_index = self._input_num_handler(input_msg, index, 1, num_of_products, allow_exit=True)
            product_index = product_index - 1 if type(product_index) == int else product_index
            
            input_msg = 'How many would you like? Please enter an amount or type in "q" or leave blank again to exit: '
            index = -1
            quantity = self._input_num_handler(input_msg, index, 1, 999, allow_exit=True) #range high set at an arbitary high number
            
            if (product_index == 'q' or product_index == '') and (len(order_basket.keys()) > 0):
                finished_selecting = True
                return order_basket
            elif (product_index == 'q' or product_index == '') and (len(order_basket.keys()) == 0):
                print('You need to have at least 1 item in your order')
                continue 
            
            # if key exists then add quantity. If it doesn't create key and set to quantity
            if order_basket.get(products[product_index].id):
                order_basket[products[product_index].id] += quantity
            else:
                order_basket[products[product_index].id] = quantity
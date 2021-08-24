from math import prod
from typing import List, Dict, Union, Callable
from customer import Customer
from product import Product
from courier import Courier
from order import Order
from is_num import is_num

class ListHelper:
    
    def __init__(self, products, couriers, orders, customers):
        self.products = products
        self.couriers = couriers
        self.orders = orders
        self.customers = customers
    
    def add_item(self, name: str, item: Union[Customer, Product, Courier, Customer]):
        items = self._list_selecter(name)
        print(f'items is {items}')
        items.append(item)
        print(f'Here is your new up-to-date list of {name}: ')
        self.show_items(name)
        
    def show_items(self, name: str):
        items = self._list_selecter(name)
        for index, item in enumerate(items, 1):
            print(f'[{index}] - {item}')
    
    def delete_item(self, name: str):
        # select the list and print out the items
        items = self._list_selecter(name)
        self.show_items(name)
        
        # set variables for the _input_num_handler func
        num_items = len(items)
        index = -1
        input_msg = 'Choose the index of the item you want to delete (Must be a valid index number)\nEnter "q" or leave blank to exit: '
        
        index = self._input_num_handler(input_msg, index, 1, num_items)
        
        if (index == 'q' or index == ''):
            return
        
        items.pop(index - 1) # reduce by 1 to account for 0 index for lists
        
        print(f'Here is the updated list:')
        self.show_items(name)
        
    def update_item(self, name: str):
        items = self._list_selecter(name)
        # loop to choose an order to change
        correct_input = False
        while correct_input == False:
            num_of_items = len(items)
            
            # show user the list of items that they can update
            self.show_items(name)
            
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
            new_value = is_num(input_msg, 'float')
            product.price = new_value
        elif product_field == '_quantity':
            new_value = is_num(input_msg, 'int')
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
        
        if order_field == 'customer_id':
            new_value = self.choose_item('customers').id
            order.customer_id = new_value
        elif order_field == 'customer_phone_number':
            new_value = self.choose_item('customers').phone_number
            order.customer_phone_number = new_value
        elif order_field == 'customer_email':
            new_value = self.choose_item('customers').email
            order.customer_phone_number = new_value
        elif order_field == 'courier_id':
            new_value = self.choose_item('couriers').id
            order.courier_id = new_value
        elif order_field == 'products':
            new_value = self.choose_products
            order.products = new_value
            
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
    
    def _list_selecter(self, name: str) -> List[Union[Product, Courier, Order, Customer]]:
        if name == 'products':
            return self.products
        elif name == 'couriers':
            return self.couriers
        elif name == 'orders':
            return self.orders
        elif name == 'customers':
            return self.customers
            
    def choose_item(self, name: str) -> Union[Courier, Customer, Order]:
        '''
        Allows for user to select a item based
        '''
        items = self._list_selecter(name)
        num_of_items = len(items)
        
        if num_of_items < 1: 
            print(f'You don\'t have any {name}!')
            return
        
        self.show_items(name)
        
        input_msg = 'Please choose a item: '
        index = -1
        index = self._input_num_handler(input_msg, index, 1, num_of_items) - 1

        return items[index]
        
    def choose_products(self) -> Dict[str, int]:
        '''
        Allows user to select products for their orders. 
        Products are appended to a dictionary
        '''
        if len(self.products) == 0:
            print('Your shop has no products you need to add some')
            return
        
        order_basket = {}

        finished_selecting = False
        while finished_selecting == False:
            self.show_items('products')
            
            input_msg = 'Please choose from the list above or type in "q" or leave blank to finish order selection: '
            index = -1
            num_of_products = len(self.products)
            
            # if product index is a number we want to reduce by 1 to index list. Can return "q" or blank as well
            product_index = self._input_num_handler(input_msg, index, 1, num_of_products, allow_exit=True)
            product_index = product_index - 1 if type(product_index) == int else product_index
            
            # allows user to leave if basket has at least 1 item
            if (product_index == 'q' or product_index == '') and (len(order_basket.keys()) > 0):
                finished_selecting = True
                return order_basket
            elif (product_index == 'q' or product_index == '') and (len(order_basket.keys()) == 0):
                print('You need to have at least 1 item in your order')
                continue 
            
            # setting the chosen products and the amount in stock to variables
            selected_product = self.products[product_index]
            selected_product_quantity = selected_product.quantity

            if selected_product_quantity < 1: 
                print(f'Sorry we have ran out of {selected_product.name}.\nPlease select something else')
                continue

            input_msg = 'How many would you like? Please enter an amount or type in "q" or leave blank again to exit: '
            index = -1
            quantity = self._input_num_handler(input_msg, index, 1, selected_product_quantity, allow_exit=True) #range high set at an arbitary high number

            # if key exists then add quantity. If it doesn't create key and set to quantity
            if order_basket.get(selected_product.id):
                order_basket[selected_product.id] += quantity
                selected_product.quantity -= quantity
            else:
                order_basket[selected_product.id] = quantity
                selected_product.quantity -= quantity
                
    def _update_quantity(item: Product, amount):
        '''
        amount can be positive or negative the quantity of the item will be reduced by this
        '''
        item.quantity += amount
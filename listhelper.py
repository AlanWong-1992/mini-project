from typing import List, Dict, Union
from customer import Customer
from product import Product
from courier import Courier

class ListHelper:
    
    def __init__(self, products, couriers, orders, customers):
        self.products = products
        self.couriers = couriers
        self.orders = orders
        self.customers = customers

    def add_item(self, item: Union[Customer, Product, Courier], items: List[Union[Customer, Product, Courier]]):
        self.items.append(item)
    
    def update_item(self, item: Union[Customer, Product, Courier], items: List[Union[Customer, Product, Courier]]):
        pass
    
    def show_items(self, item: Union[Customer, Product, Courier], items: List[Union[Customer, Product, Courier]]):
        self.items.append(item)
    
    def delete_item(self, item: Union[Customer, Product, Courier], items: List[Union[Customer, Product, Courier]]):
        self.items.append(item)
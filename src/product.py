from create_id import create_id
from is_num import is_num
from typing import Callable

class Product():
    
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
    
    def __repr__(self):
        return f'id: {self.id} | name: {self.name} | price: {self.price} | quantity: {self.quantity}'
        
    # used to instantiate an object from user input
    @classmethod
    def create_product_user(self, create_id: str):
        correct_input = False
        
        while correct_input == False:
            try:
                id = create_id()
                name = input('What is the name of the product? ')
                price = is_num('How much does it cost? ', 'float')
                quantity = is_num('How many do we have in stock? ', 'int')
                return self(id, name, price, quantity)
            
            except Exception as e:
                print(f'There was an error {e}')
                continue
            
    # id
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
        
    @id.deleter
    def id(self):
        del self._id
        
    # name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @name.deleter
    def name(self):
        del self._name
    
    # price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
        
    @price.deleter
    def price(self):
        del self._price
    
    # quantity
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        
    @quantity.deleter
    def quantity(self):
        del self._quantity
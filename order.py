from typing import List, Dict
from courier import Courier
from customer import Customer
from product import Product
from create_id import create_id
# from list_helper import ListHelper

class Order():
    
    def __init__(self, id, customer_id: str, customer_phone_number: str, customer_email: str, courier_id: str, products: Dict[str, int]):
        self.id = id
        self.customer_id = customer_id
        self.customer_phone_number = customer_phone_number
        self.customer_email = customer_email
        self.courier_id = courier_id
        self.products = products
        
    def __repr__(self):
        return f'id: {self.id} | customer id: {self.customer_id} | customer phone number: {self.customer_phone_number} | customer email: {self.customer_email} | courier id: {self.courier_id} | products: {self.products}'

    # used to instantiate an object from user input
    # @classmethod
    # def create_order_user(self, create_id, customer: Customer, courier_id: str, products: Dict[str, int]):
    #     correct_input = False
    #     while correct_input == False:
    #         try:
    #             id = create_id()
    #             return self(id, customer.id, customer.phone_number, customer.email, courier_id, products)
    #         except Exception as e:
    #             print(f'There was an error {e}')
    #             continue
    
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
        
    # first name
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        
    @first_name.deleter
    def first_name(self):
        del self._first_name
        
    # last name
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
        
    @last_name.deleter
    def last_name(self):
        del self._last_name
    
    # phone number
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
        
    @phone_number.deleter
    def phone_number(self):
        del self._phone_number
    
    # email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
        
    @email.deleter
    def email(self):
        del self._email

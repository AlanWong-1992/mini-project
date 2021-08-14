from typing import List
from courier import Courier
from customer import Customer
from create_id import create_id
from list_helper import ListHelper

class Order():
    
    def __init__(self, id: str, customer_id: str, courier_id: str, customer_phone_number: str, customer_email: str, create_id: callable):
        self.create_id = create_id
        self.id = id
        self.customer_id = customer_id
        self.courier_id = courier_id
        self.customer_phone_number = customer_phone_number
        self.customer_email = customer_email
        
    def __repr__(self):
        return f'id: {self.id} | customer id: {self.customer_id} | customer phone number: {self.customer_phone_number} | customer email: {self.customer_email}'

    # used to instantiate an object from user input
    @classmethod
    def create_order_user(self, create_id, couriers: List[Courier], list_helper: ListHelper):
        correct_input = False
        while correct_input == False:
            try:
                id = create_id()
                customer = Customer.create_customer_user(create_id)
                # print(f'The order ID is {id}')
                # print(customer)
                courier_id = list_helper.choose_courier(couriers)
                print(f'the returned value of choose_courier is {courier}')
                return
                # first_name = input('What is the first name? ')
                # last_name = input('What is the last name? ')
                # phone_number = input('What is the phone number? ')
                # email = input('What is the email? ')
                # return self(id, first_name, last_name, phone_number, email)
            
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
        
# apple_muffin = Courier.create_product()
# order = Courier('Usain', 'Bolt', '079883294729', 'usain@bolt.com')
# print(f'Courier: {order.first_name} {order.last_name}, {order.phone_number}, {order.email}')
# print(f'id is {order.id}')

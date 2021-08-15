from item import Item
from create_id import create_id

class Customer(Item):
    
    def __init__(self, id, first_name, last_name, phone_number, address, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
    
    def __repr__(self):
        return f'id: {self.id} | first name: {self.first_name} | last name: {self.last_name} | phone_number: {self.phone_number} | address: {self.address} | email: {self.email}'
    
    @classmethod
    def create_customer_user(self, create_id):
        correct_input = False
        
        while correct_input == False:
            try:
                id = create_id()
                first_name = input('What is the first name? ')
                last_name = input('What is the last name? ')
                phone_number = input('What is the phone number? ')
                address = input('What is the address? ')
                email = input('What is the email address? ')
                return self(id, first_name, last_name, phone_number, address, email)
            
            except Exception as e:
                print('Invalid Input')
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
    
    # address
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value
        
    @address.deleter
    def address(self):
        del self._address
        
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
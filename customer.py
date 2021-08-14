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
            
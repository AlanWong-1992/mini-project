from item import Item

class Customer(Item):
    
    def __init__(self, first_name, last_name, phone_number, address, email, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.id = id
    
    @classmethod
    def get_user_input(self):
        correct_input = False
        
        while correct_input == False:
            try:
                first_name = input('What is the first name? ')
                last_name = input('What is the last name? ')
                phone_number = input('What is the phone number? ')
                address = input('What is the address? ')
                email = input('What is the email address? ')
                return self(first_name, last_name, phone_number, address, email)
            
            except Exception as e:
                print('Invalid Input')
                continue
class Product:
    
    def __init__(self, name, price, quantity, id=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = id
    
    # used to instantiate an object from user input
    @classmethod
    def create_product(self):
        correct_input = False
        
        while correct_input == False:
            try:
                name = input('What is the name of the product? ')
                price = input('How much does it cost? ')
                quantity = input('How many do we have in stock? ')
                return self(name, price, quantity)
            
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
    
    # quanitity
    @property
    def quanitity(self):
        return self._quanitity
    
    @quanitity.setter
    def quanitity(self, value):
        self._quanitity = value
        
    @quanitity.deleter
    def quanitity(self):
        del self._quanitity
        
# # apple_muffin = Product.create_product()
# product_1 = Product('apple muffin', 2.90, 20)
# print(f'This is your apple_muffin: {product_1.name}, {product_1.price}, {product_1.quantity}')
# print(product_1.name)
# product_1.name = 'pear muffin'
# del product_1.name
# print(product_1.price)
# product_1.name = 'banana muffin'
# print(product_1.name)
# print(product_1.id)
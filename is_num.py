from typing import Union

def is_num(input_msg: str, type: str) -> Union[float, int]:
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
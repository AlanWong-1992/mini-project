class Menu:
    def __init__(self):
        print('Menu class has been instantiated')

    def main_menu_choice(self):
        input_is_correct = False
        
        while input_is_correct == False:
            try:
                choice = int(input('\nPlease choose an option by selecting a number:\n'
                                    '0) Exit this Application\n'
                                    '1) See Product Menu Options\n'
                                    '2) See Courier Options\n'
                                    '3) See Order Options\n'
                                    'Please enter a number from the options above: '))
                if (type(choice) == int and choice <= 3 and choice >= 0):
                    input_is_correct = True
                else:
                    print('You need to pick one of the numbers above')
            except ValueError:
                print('You need to enter one of the numbers above')
                input_is_correct = False
                
        return choice
        
menu = Menu()
menu.main_menu_choice()
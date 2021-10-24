from unittest.mock import patch
from .. src.menu-2 import Menu

# class Menu:
#     def __init__(self):
#         print('Menu class has been instantiated')

#     def main_menu_choice(self):
#         input_is_correct = False
        
#         while input_is_correct == False:
#             try:
#                 choice = int(input('\nPlease choose an option by selecting a number:\n'
#                                     '0) Exit this Application\n'
#                                     '1) See Product Menu Options\n'
#                                     '2) See Courier Options\n'
#                                     '3) See Order Options\n'
#                                     'Please enter a number from the options above: '))
#                 if (type(choice) == int and choice <= 3 and choice >= 0):
#                     input_is_correct = True
#                 else:
#                     print('You need to pick one of the numbers above')
#             except ValueError:
#                 print('You need to enter one of the numbers above')
#                 input_is_correct = False
#             except Exception as e:
#                 print(f'There is an error {str(e)}')
#                 input_is_correct = False
                
#         return choice

class Test_Menu:
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[0, 4, 1, 2])
    def test_main_menu_choice(self, mock_input, mock_print) -> int:
        menu = Menu()

        # mock_input.return_value = 0
        assert menu.main_menu_choice() == 0
        
        # mock_input.side_effect = [4, 1]
        menu.main_menu_choice()
        mock_print.assert_called_with('You need to pick one of the numbers above')

        # mock_input.return_value = 2
        assert menu.main_menu_choice() == 2
        assert mock_input.call

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[0, 4, 1, 2])
    def test_main_menu_choice(self, mock_input, mock_print) -> int:
        menu = Menu()

        # mock_input.return_value = 0
        assert menu.main_menu_choice() == 0
        
        # mock_input.side_effect = [4, 1]
        menu.main_menu_choice()
        mock_print.assert_called_with('You need to pick one of the numbers above')

        # mock_input.return_value = 2
        assert menu.main_menu_choice() == 2
        assert mock_input.call
    
    

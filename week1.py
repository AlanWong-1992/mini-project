products = ['Coke Zero', 'Sprite', 'Fanta', 'Pepsi']

run_menu = True

while run_menu:
    
    # first user input is to either exit the application or to see product menu options
    print('\nPlease choose an option by selecting a number:\n0) Exit this menu\n1) See Product Menu Options')
    choice_1 = int(input('Please enter a number from the options above: '))
    if (choice_1 == 0):
        print('\nExiting Application')
        run_menu = False
    elif (choice_1 == 1):
        # 5 different options for CRUD and to return to previous menu
        print('\nPlease choose an option by selecting a number:\n0) Exit this menu\n1) Add a product\n2) View all products\n3) Update a Product\n4) Delete a product\n')
        choice_2 = int(input('Please select a number from the above options: '))
        
        # 0 means returning to the previous menu
        if (choice_2 == 0):
            print('\nReturning to main Menu')
            continue
        
        # 1 means Creating and adding a new product to the product list    
        elif (choice_2 == 1):
            new_product_name = str(input('\nPlease enter a new product name: '))
            products.append(new_product_name)
            print(f'Updated products: {products}')
            
        # 2 means Retreiving the current product list
        elif (choice_2 == 2):
            print(f'\nHere is a list of products: {products}.\n')
            
        # 3 means Updating a product chosen from the product list
        elif (choice_2 == 3):
            print(f'\nHere is a list of products: {products}.\n')
            index_to_update = int(input('Choose the index of the item you want to change (first item starts at 0): '))
            new_product_name = str(input('Please choose a new product name: '))
            products[index_to_update] = new_product_name
            print(f'Updated products: {products}')
            
        # 4 means Deleting a product from the product list
        elif (choice_2 == 4):
            print(f'\nHere is a list of products: {products}.\n')
            index_to_delete = int(input('Choose the index of the item you want to Delete: '))
            products.pop(index_to_delete)
            print(f'Updated products: {products}')
exit()
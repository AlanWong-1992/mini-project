# # add some product names
# CREATE products list
products = ['Coke Zero', 'Sprite', 'Fanta', 'Pepsi']

# PRINT main menu options
print('Please choose an option by selecting a number:\n0) Exit this menu\n1) See Product Menu Options')
# GET user input for main menu option
choice_1 = int(input('Please enter a number from the options above: '))
# IF user input is 0:
    # EXIT app
if (choice_1 == 0):
    print('Exiting menu')
    exit()

# # products menu
# ELSE IF user input is 1:
elif (choice_1 == 1):
    # PRINT product menu options
    print('Please choose an option by selecting a number:\n0) Exit this menu\n1) Add a product\n2) View all products\n3) Update a Product\n4) Delete a product\n')
    # GET user input for product menu option
    choice_2 = int(input('Please select a number from the above options'))
    # IF user input is 0:
        # RETURN to main menu
    if (choice_2 == 0):
        print('Returning to main Menu')    
    # ELSE IF user input is 1:
        # PRINT products list
    elif (choice_2 == 1):
        print(products)
    # ELSE IF user input is 2:
    elif (choice_2 == 2):
        new_product_name = str(input('Please enter a new product name'))
        products.append(new_product_name)
        print(f'Updated products: {products}')
        # # CREATE new product
        # GET user input for product name
    # APPEND product name to products list
    
    # ELSE IF user input is 3:
    elif (choice_2 == 3):
        print(f'Here is a list of products: {products}.\n')
        index_to_update = int(input('Choose the index of the item you want to change (first item starts at 0): '))
        new_product_name = str(input('Please choose a new product name: '))
        products[index_to_update] = new_product_name
        print(f'Updated products: {products}')
        # # STRETCH GOAL - UPDATE existing product
        # PRINT product names with its index value
        # GET user input for product index value
        # GET user input for new product name
        # UPDATE product name at index in products list
    
    # ELSE IF user input is 4:
    elif (choice_2 == 4):
        print(f'Here is a list of products: {products}.\n')
        index_to_delete = int(input('Choose the index of the item you want to Delete: '))
        products.pop(index_to_delete)
        print(f'Updated products: {products}')
        # # STRETCH GOAL - DELETE product
        # PRINT products list
        # GET user input for product index value
        # DELETE product at index in products list
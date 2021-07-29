import menu

# populating lists from files
products_file = './products.json'
couriers_file = './couriers.json'
orders_file = './orders.json'
products = menu.read_from_file(products_file, to_json=True)
couriers = menu.read_from_file(couriers_file, to_json=True)
orders = menu.read_from_file(orders_file, to_json=True)

# print(f'Products is a {type(products)}. Here is a list of your products: {products}')
# print(f'Couriers is a {type(couriers)} Here is a list of your couriers: {couriers}')
# print(f'Orders is a {type(orders)} and Here is a list of your orders: {orders}')

run_menu = True

while run_menu:
    '''Get user input and decide what options to take'''
    
    main_menu_choice = menu.main_menu_choice()
    
    # exits the application and saves to .txt files    
    if (main_menu_choice == 0):
        menu.write_to_file(products_file, products, to_json=True)
        menu.write_to_file(couriers_file, couriers, to_json=True)
        menu.write_to_file(orders_file, orders, to_json=True)
        print('\nExiting and saving application! See you next time.')
        run_menu = False
    
    # product options
    elif (main_menu_choice == 1):
        sub_menu_choice = menu.sub_menu_choice('product')
            
        # returns to previous menu
        if (sub_menu_choice == 0):
            print('\nReturning to main Menu')
            continue
        
        # add a new product to products
        elif (sub_menu_choice == 1):
            menu.add_product(products)
            
        # retrieve the current product list
        elif (sub_menu_choice == 2):
            menu.show_items('product', products)
            
        # update a product chosen from the product list
        elif (sub_menu_choice == 3):
            menu.update_item('product', products)
            
        # deleting a product from the product list
        elif (sub_menu_choice == 4):
            menu.remove_item('product', products)
    
    # courier options    
    elif (main_menu_choice == 2):
        
        # user chooses an option
        sub_menu_choice = sub_menu_choice = menu.sub_menu_choice('courier')
                
        # return to the previous menu
        if (sub_menu_choice == 0):
            print('\nReturning to main Menu')
            continue
        
        # adding a new courier to the courier list    
        elif (sub_menu_choice == 1):
            menu.add_courier(couriers)
            
        # retreiving the current courier list
        elif (sub_menu_choice == 2):
            menu.show_items('courier', couriers)
            
        # updating a courier chosen from the courier list
        elif (sub_menu_choice == 3):
            menu.update_item('courier', couriers)
            
        # deleting a courier from the courier list
        elif (sub_menu_choice == 4):
            menu.remove_item('courier', couriers)
    
    # order options    
    elif (main_menu_choice == 3):
        
        # user chooses an option
        sub_menu_choice = menu.sub_menu_choice('order')
                
        # return to the previous menu
        if (sub_menu_choice == 0):
            print('\nReturning to main Menu')
            continue
        
        # adding a new order to the order list    
        elif (sub_menu_choice == 1):
            menu.add_order(couriers, orders, menu.create_order_id)
            print(f'read_from_fileHere are your orders: {orders}')
            
        # retreiving the current order list
        elif (sub_menu_choice == 2):
            menu.show_items('order', orders)
            
        # updating a order chosen from the order list
        elif (sub_menu_choice == 3):
            menu.update_order('order', orders)
            
        # deleting a order from the order list
        elif (sub_menu_choice == 4):
            menu.remove_item('order', orders)    
exit()
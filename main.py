import menu

# variables
products = []
couriers = []
orders = []
products_file = 'products.txt'
couriers_file = 'couriers.txt'
orders_file = 'orders.json'

# populate products and couriers lists
menu.populate_items(products_file, products)
menu.populate_items(couriers_file, couriers)
menu.populate_items(orders_file, orders)

print(f'Here is a list of your products: {products}')
print(f'Here is a list of your couriers: {couriers}')
print(f'Here is a list of your orders: {orders}')

run_menu = True

while run_menu:
    '''Get user input and decide what options to take'''
    
    main_menu_choice = menu.main_menu_choice()
    
    # exits the application and saves to .txt files    
    if (main_menu_choice == 0):
        menu.save_items(products_file, products)
        menu.save_items(couriers_file, couriers)
        menu.save_items(orders_file, orders, True)
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
            menu.add_item('product', products)
            
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
            menu.add_item('courier', couriers)
            
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
        sub_menu_choice = sub_menu_choice = menu.sub_menu_choice('order')
                
        # return to the previous menu
        if (sub_menu_choice == 0):
            print('\nReturning to main Menu')
            continue
        
        # adding a new order to the order list    
        elif (sub_menu_choice == 1):
            menu.add_order(couriers, orders)
            print(f'Here are your orders: {orders}')
            
        # retreiving the current order list
        elif (sub_menu_choice == 2):
            menu.show_items('order', orders)
            
        # updating a order chosen from the order list
        elif (sub_menu_choice == 3):
            menu.update_item('order', orders)
            
        # deleting a order from the order list
        elif (sub_menu_choice == 4):
            menu.remove_item('order', orders)    
exit()
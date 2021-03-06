import menu
import pymysql
import os
from db_helper import DBHelper
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# instantiate DB object
db_helper = DBHelper(host, user, password, database)

# populating lists from files
products_file = './products.csv'
couriers_file = './couriers.csv'
orders_file = './orders.csv'
products = menu.read_from_file(products_file)
couriers = menu.read_from_file(couriers_file)
orders = menu.read_from_file(orders_file)

print(f'Products is a {type(products)}. Here is a list of your products: {products}')
print(f'Couriers is a {type(couriers)} Here is a list of your couriers: {couriers}')
print(f'Orders is a {type(orders)} and Here is a list of your orders: {orders}')

run_menu = True

while run_menu:
    '''Get user input and decide what options to take'''
    
    main_menu_choice = menu.main_menu_choice()
    
    # exits the application and saves to .txt files    
    if (main_menu_choice == 0):
        menu.write_to_file(products_file, products)
        menu.write_to_file(couriers_file, couriers)
        menu.write_to_file(orders_file, orders)
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
            menu.add_product(db_helper)
            
        # retrieve the current product list
        elif (sub_menu_choice == 2):
            menu.show_items('product', 'product', db_helper)
            
        # update a product chosen from the product list
        elif (sub_menu_choice == 3):
            menu.update_product(db_helper)
            
        # deleting a product from the product list
        elif (sub_menu_choice == 4):
            menu.remove_item('product', 'product', db_helper)
    
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
            menu.add_courier(db_helper)
            
        # retreiving the current courier list
        elif (sub_menu_choice == 2):
            menu.show_items('courier', 'courier', db_helper)
            
        # updating a courier chosen from the courier list
        elif (sub_menu_choice == 3):
            menu.update_courier(db_helper)
            
        # deleting a courier from the courier list
        elif (sub_menu_choice == 4):
            menu.remove_item('courier', 'courier', db_helper)
    
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
            menu.add_order(db_helper)
            # print(f'read_from_fileHere are your orders: {orders}')
            
        # retreiving the current order list
        elif (sub_menu_choice == 2):
            view_order_choice = menu.view_orders_choice()
            
            if(view_order_choice == 1):
                order_id = menu.show_all_orders('order_info','order_product', db_helper)
                # see_order_products = input('Would you like to see the products for this order? [y/n]')
                # if see_order_products
            elif(view_order_choice == 2):
                menu.show_orders_by_status(db_helper)
            elif(view_order_choice == 3):
                menu.show_orders_by_courier(db_helper)
            
        # updating a order chosen from the order list
        elif (sub_menu_choice == 3):
            print(couriers)
            # menu.update_item('order', orders, products=products, couriers=couriers)
            menu.update_order(db_helper)
                        
        # deleting a order from the order list
        elif (sub_menu_choice == 4):
            menu.remove_item('order', 'order_info', db_helper)
exit()
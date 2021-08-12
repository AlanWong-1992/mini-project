import menu
import pymysql
import os
from product import Product
from listhelper import ListHelper
from db_helper import DBHelper
from dotenv import load_dotenv

# populating lists from files
products_file = './products.csv'
couriers_file = './couriers.csv'
orders_file = './orders.csv'
products = menu.read_from_file(products_file)
couriers = menu.read_from_file(couriers_file)
orders = menu.read_from_file(orders_file)
customers = []

print(f'Products is a {type(products)}. Here is a list of your products: {products}')
print(f'Couriers is a {type(couriers)} Here is a list of your couriers: {couriers}')
print(f'Orders is a {type(orders)} and Here is a list of your orders: {orders}')
print(f'Orders is a {type(customers)} and Here is a list of your customers: {customers}')

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# instantiate DB and List Helper objects
db_helper = DBHelper(host, user, password, database)
list_helper = ListHelper()

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
            product = Product.create_product_user()
            list_helper.add_item(product, products)
            
        # retrieve the current product list
        elif (sub_menu_choice == 2):
            list_helper.show_items(products)
            
        # update a product chosen from the product list
        elif (sub_menu_choice == 3):
            list_helper.update_item(products)
            
        # deleting a product from the product list
        elif (sub_menu_choice == 4):
            list_helper.delete_item(products)
    
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
            menu.add_order(products, couriers, orders, menu.create_order_id)
            print(f'read_from_fileHere are your orders: {orders}')
            
        # retreiving the current order list
        elif (sub_menu_choice == 2):
            view_order_choice = menu.view_orders_choice()
            
            if(view_order_choice == 1):
                menu.show_items('order', orders)
            elif(view_order_choice == 2):
                menu.show_orders_by_status(orders)
            elif(view_order_choice == 3):
                menu.show_orders_by_courier(orders, couriers=couriers)
            
        # updating a order chosen from the order list
        elif (sub_menu_choice == 3):
            print(couriers)
            menu.update_item('order', orders, products=products, couriers=couriers)
            
        # deleting a order from the order list
        elif (sub_menu_choice == 4):
            menu.remove_item('order', orders)
exit()
from create_id import create_id
import menu
import pymysql
import os
from product import Product
from courier import Courier
from order import Order
from customer import Customer
from list_helper import ListHelper
from db_helper import DBHelper
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# instantiate DB and List Helper objects
db_helper = DBHelper(host, user, password, database)

# populating lists from files
products_file = './products.csv'
couriers_file = './couriers.csv'
orders_file = './orders.csv'
customers_file = './customers.csv'
products = menu.read_from_file('products', products_file)
couriers = menu.read_from_file('couriers', couriers_file)
orders = menu.read_from_file('orders', orders_file)
customers = menu.read_from_file('customers', customers_file)

list_helper = ListHelper(products, couriers, orders, customers)
print(f'self.products: {list_helper.products}')

# print(f'Products is a {type(products)}. Here is a list of your products: {products}')
# print(f'Couriers is a {type(couriers)} Here is a list of your couriers: {couriers}')
# print(f'Orders is a {type(orders)} and Here is a list of your orders: {orders}')
# print(type(orders[0].products))
# print(f'Orders is a {type(customers)} and Here is a list of your customers: {customers}')

run_menu = True

while run_menu:
    '''Get user input and decide what options to take'''
    
    main_menu_choice = menu.main_menu_choice()
    
    # exits the application and saves to .txt files    
    if (main_menu_choice == 0):
        menu.write_to_file(products_file, products)
        menu.write_to_file(couriers_file, couriers)
        menu.write_to_file(orders_file, orders)
        menu.write_to_file(customers_file, customers)
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
            product = Product.create_product_user(create_id)
            list_helper.add_item('products', product)

        # retrieve the current product list
        elif (sub_menu_choice == 2):
            list_helper.show_items('products')
            
        # update a product chosen from the product list
        elif (sub_menu_choice == 3):
            list_helper.update_item('products')
            
        # deleting a product from the product list
        elif (sub_menu_choice == 4):
            list_helper.delete_item('products')
    
    # courier options
    elif (main_menu_choice == 2):
        sub_menu_choice = menu.sub_menu_choice('courier')
            
        # returns to previous menu
        if (sub_menu_choice == 0):
            print('\nReturning to main Menu')
            continue
        
        # add a new courier to couriers
        elif (sub_menu_choice == 1):
            courier = Courier.create_courier_user(create_id)
            list_helper.add_item('couriers', courier)

        # retrieve the current courier list
        elif (sub_menu_choice == 2):
            list_helper.show_items('couriers')
            
        # update a courier chosen from the courier list
        elif (sub_menu_choice == 3):
            list_helper.update_item('couriers')
            
        # deleting a courier from the courier list
        elif (sub_menu_choice == 4):
            list_helper.delete_item('couriers')
            
    # order options
    elif (main_menu_choice == 3):
        sub_menu_choice = menu.sub_menu_choice('order')
            
        # returns to previous menu
        if (sub_menu_choice == 0):
            print('\nReturning to main Menu')
            continue
        
        # add a new order to orders
        elif (sub_menu_choice == 1):
            # arguments for the Order object
            order_id = create_id()
            customer = Customer.create_customer_user(create_id)
            courier_id = list_helper.choose_item(couriers)
            products = list_helper.choose_products(products)
            
            # creating the order and appending the order and customer objs to their lists
            order = Order(order_id, customer.id, customer.phone_number, customer.email, courier_id, products)
            list_helper.add_item(customer, customers)
            list_helper.add_item(order, orders)

        # retrieve the current order list
        elif (sub_menu_choice == 2):
            list_helper.show_items(orders)
            
        # update a order chosen from the order list
        elif (sub_menu_choice == 3):
            list_helper.update_item('orders', orders)
            
        # deleting a order from the order list
        elif (sub_menu_choice == 4):
            list_helper.delete_item(orders)
    
    # # order options    
    # elif (main_menu_choice == 3):
        
    #     # user chooses an option
    #     sub_menu_choice = menu.sub_menu_choice('order')
                
    #     # return to the previous menu
    #     if (sub_menu_choice == 0):
    #         print('\nReturning to main Menu')
    #         continue
        
    #     # adding a new order to the order list    
    #     elif (sub_menu_choice == 1):
    #         menu.add_order(products, couriers, orders, menu.create_order_id)
    #         print(f'read_from_fileHere are your orders: {orders}')
            
    #     # retreiving the current order list
    #     elif (sub_menu_choice == 2):
    #         view_order_choice = menu.view_orders_choice()
            
    #         if(view_order_choice == 1):
    #             menu.show_items('order', orders)
    #         elif(view_order_choice == 2):
    #             menu.show_orders_by_status(orders)
    #         elif(view_order_choice == 3):
    #             menu.show_orders_by_courier(orders, couriers=couriers)
            
    #     # updating a order chosen from the order list
    #     elif (sub_menu_choice == 3):
    #         print(couriers)
    #         menu.update_item('order', orders, products=products, couriers=couriers)
            
    #     # deleting a order from the order list
    #     elif (sub_menu_choice == 4):
    #         menu.remove_item('order', orders)
exit()
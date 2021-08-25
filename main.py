from create_id import create_id
import menu
import pymysql
import os
from product import Product
from courier import Courier
from order import Order
from customer import Customer
from csv_helper import CSVHelper
from list_helper import ListHelper
from is_num import is_num
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
products_file = './data/products.csv'
couriers_file = './data/couriers.csv'
orders_file = './data/orders.csv'
customers_file = './data/customers.csv'
csv_helper = CSVHelper(products_file, couriers_file, orders_file, customers_file)
products = csv_helper.read_from_file('products', csv_helper.products_file)
couriers = csv_helper.read_from_file('couriers', csv_helper.couriers_file)
orders = csv_helper.read_from_file('orders', csv_helper.orders_file)
customers = csv_helper.read_from_file('customers', csv_helper.customers_file)

list_helper = ListHelper(products, couriers, orders, customers)

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

            # set courier_id to courier if the return value exists. Otherwise set to 0.
            courier = list_helper.choose_item('couriers')

            if courier:
                courier_id = courier.id
            else:
                print('You need to add some couriers before adding an order')
            
            # choosing the products
            basket = list_helper.choose_products()
            
            if basket == None:
                print('Your shop has no basket to sell. Please add some before adding any orders')
                continue

            # creating the order and appending the order and customer objs to their lists
            order = Order(order_id, customer.id, customer.phone_number, customer.email, courier_id, basket)
            list_helper.add_item('customers', customer)
            list_helper.add_item('orders', order)

        # retrieve the current order list
        elif (sub_menu_choice == 2):
            list_helper.show_items('orders')
            
        # update a order chosen from the order list
        elif (sub_menu_choice == 3):
            list_helper.update_item('orders')
            
        # deleting a order from the order list
        elif (sub_menu_choice == 4):
            list_helper.delete_item('orders')

exit()
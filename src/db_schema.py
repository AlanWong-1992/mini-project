import mysql.connector
import os
from db_helper import DBHelper
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

drop_tables_sql = \
    """
    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS couriers;
    DROP TABLE IF EXISTS customers;
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS order_baskets;
    """

create_tables_sql = \
    """
    CREATE TABLE products(
        product_id VARCHAR(16) PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        price FLOAT(4, 2) NOT NULL,
        stock INT NOT NULL
    );
    CREATE TABLE couriers(
        courier_id VARCHAR(16) PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        email VARCHAR(70) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
    );
    CREATE TABLE customers(
        customer_id VARCHAR(16) PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        email VARCHAR(70) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
    );
    CREATE TABLE orders(
        order_id VARCHAR(16) PRIMARY KEY,
        courier_id VARCHAR(16),
        customer_id VARCHAR(16),
        CONSTRAINT FK_courier_order FOREIGN KEY (courier_id) 
        REFERENCES couriers(courier_id),
        CONSTRAINT FK_customer_order FOREIGN KEY (customer_id) 
        REFERENCES customers(customer_id)
    ); 
    CREATE TABLE order_baskets(
        order_id VARCHAR(16),
        product_id VARCHAR(16),
        quantity int NOT NULL,
        CONSTRAINT FK_order_order_basket FOREIGN KEY (order_id) 
        REFERENCES orders(order_id),
        CONSTRAINT FK_product_order_basket FOREIGN KEY (product_id)
        REFERENCES products(product_id),
        PRIMARY KEY (order_id, product_id)
    )
    """

conn = DBHelper(host, user, password, database)

print(conn)
print(database)

conn.no_commit_execute(drop_tables_sql)
conn.no_commit_execute(create_tables_sql)

# def table_creation(database: str):
#    connectdb = database_connection(database=database)
#    connectdb.autocommit = True
#    cursor = connectdb.cursor()
#    create_items_table = \
#    """
#    DROP TABLE IF EXISTS items cascade;
#    CREATE TABLE Items(
#       item_id SERIAL,
#       item_name VARCHAR NOT NULL UNIQUE,
#       item_price DECIMAL,
#       PRIMARY KEY(item_id)
#    );"""
#    create_stores_table = \
#       """
#       DROP TABLE IF EXISTS stores cascade;
#       CREATE TABLE Stores(
#             store_id SERIAL,
#             store_name VARCHAR NOT NULL UNIQUE,
#             PRIMARY KEY(store_id)
#       );"""
#    create_orders_table = \
#       """
#       DROP TABLE IF EXISTS orders cascade;
#       CREATE TABLE Orders(
#          transaction_id VARCHAR,
#          item_id INTEGER,
#          quantity INTEGER,
#          PRIMARY KEY(transaction_id, item_id),
#          CONSTRAINT fk_transactions
#             FOREIGN KEY(transaction_id)
#                REFERENCES Transactions(transaction_id) ON UPDATE CASCADE,
#          CONSTRAINT fk_items
#             FOREIGN KEY(item_id)
#                REFERENCES Items(item_id) ON UPDATE CASCADE
#       );"""
#    # PostgreSQL uses the  yyyy-mm-dd
#    create_transactions_table = \
#       """
#       DROP TABLE IF EXISTS transactions cascade;
#       CREATE TABLE Transactions(
#             transaction_id VARCHAR NOT NULL,
#             date_time TIMESTAMP, 
#             store_id INTEGER,
#             cash_or_card VARCHAR NOT NULL,
#             total_price DECIMAL,
#             PRIMARY KEY(transaction_id),
#             CONSTRAINT fk_stores
#                FOREIGN KEY(store_id)
#                   REFERENCES Stores(store_id) ON UPDATE CASCADE
#             );"""
#    print("creating items table...")
#    cursor.execute(create_items_table)
#    print('success')
#    print("creating stores table...")
#    cursor.execute(create_stores_table)
#    print('success')
#    print("creating transactions table...")
#    cursor.execute(create_transactions_table)
#    print('success')
#    print("creating orders table...")
#    cursor.execute(create_orders_table)
#    print('success')
#    connectdb.close()
# database_connection()

# table_creation(database="root")
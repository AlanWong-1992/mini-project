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
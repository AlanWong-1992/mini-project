import csv
from typing import List, Union
from product import Product
from courier import Courier
from order import Order
from customer import Customer

class CSVHelper:

    def __init__(self, products_file, couriers_file, orders_file, customers_file):
        self.products_file = products_file
        self.couriers_file = couriers_file
        self.orders_file = orders_file
        self.customers_file = customers_file

    def write_to_file(filepath: str, items: List[Union[Product, Courier, Order, Customer]]):
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as file:
                keys = vars(items[0]).keys()
                writer = csv.DictWriter(file, keys)
                writer.writeheader()
                for item in items:
                    print(vars(item))
                    writer.writerow(vars(item))
        except Exception as e:
                print(f'There is an error {str(e)}')

    # reading files and populate list items            
    def read_from_file(name: str, filepath: str) -> List[Union[Product, Courier, Order, Customer]]:
        try:
            file_items = []
            with open(filepath, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for line in reader:
                    if name == 'products':
                        print(f'line 0 is {line[0]}, line 1 is {line[1]}, line 2 is {line[2]}, line 3 is {line[3]}')
                        file_items.append(Product(line[0], line[1], line[2], line[3]))
                    elif name == 'couriers':
                        file_items.append(Courier(line[0], line[1], line[2], line[3], line[4]))
                    elif name == 'orders':
                        file_items.append(Order(line[0], line[1], line[2], line[3], line[4], ast.literal_eval(line[5])))
                    elif name == 'customers':
                        file_items.append(Customer(line[0], line[1], line[2], line[3], line[4], line[5]))
            return file_items
        except FileNotFoundError as fnfe:
            print(f'Your file was not found')
            return []
        except Exception as e:
            print(f'There was an error {e}. Returning an empty list')
            return []
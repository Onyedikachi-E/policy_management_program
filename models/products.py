"""
Task 3 : Product Management: - Implement methods for creating, updating, and removing/suspending policy products.
"""


class Product:
    def __init__(self, product_name, product_code, price):
        self.product_name = product_name
        self.product_code = product_code
        self.price = price


    def create_product(self, products_database):
        "*To create a new product*"

        try:
            if not self.product_code in products_database:
                products_database[self.product_code] = self
            else:
                print(f"Product name {self.product_name} already exist with product code {self.product_code}")
            
        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


    def update_product(self, product_name=None, price=None):
        "*To update an existing product*"

        try:
            if product_name is None and price is not None:
                self.price = price
            elif product_name is not None and price is None:
                self.product_name = product_name
            elif product_name is not None and price is not None:
                self.product_name = product_name; self.price = price
            else:
                print("There is no data supplied")
        
        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


    def remove_product(self, products_database:dict):
        "*To update an existing product*"

        try:
            products_database.pop(self.product_code)
            print(f"The product {self.product_name} has been removed")

        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)
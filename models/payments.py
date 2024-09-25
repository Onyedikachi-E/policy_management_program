"""
Task 2 : Payment Management: - Implement methods for payment processing, reminders, and penalties.
"""
from models.policyholders import PolicyHolder
from models.products import Product
from datetime import date, datetime


class Payments:
    def __init__(self, product:Product, policy_holder:PolicyHolder, due_date:date):
        self.product = product
        self.policy_holder = policy_holder
        self.due_date = due_date


    def processing_payment(self, payments_database:dict):
        "*To process payment*"

        try:
            if self.policy_holder.account_balance >= self.product.price:
                self.policy_holder.account_balance -= self.product.price
                payments_database[self.product.product_code] = (payments_database.get(self.product.product_code, {}) | {self.policy_holder.policy_number : self})
                print(f"Payment of {self.product.product_name} by {self.policy_holder.fname} {self.policy_holder.lname} is successful")
            else:
                print("Your account balance is too low to pay for this product")
            
        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


    def payment_reminders(self):
        "*To remind policy holders of product payment 7 days before due date*"

        if datetime.now().date() - self.due_date == 7:
             print(f"Dear {self.policy_holder.fname} {self.policy_holder.lname}, your {self.product.product_name} will expire in 7 days on {datetime.strftime(self.due_date), '%d-%m-%Y'}. Kindly renew payment!!")


    def payment_penalties(self, policy_holders_database:dict):
        "*To give penalties to defaulters*"
        
        try:
            #Check if due date has passed and suspend the account
            if datetime.now().date() > self.due_date:
                        self.policy_holder.suspend_policy_holder(policy_holders_database=policy_holders_database)
                        print(f"The account of {self.policy_holder.fname} {self.policy_holder.lname} has been suspended for failure to pay {self.product.product_name} before due date")
        
        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


# This functions checks the payments_database and calls the payment_penalties() method for each payment object
def check_defaulters(payments_database:dict, policy_holders_database:dict):
    "*To check defaulters*"

    try:
        for product_code, payment_record in payments_database.items():
            for policy_holder_number, payment_data in payment_record.items():
                payment_data.payment_penalties(policy_holders_database)
            
    # Error Handling for Exception
    except Exception as e:
        # Error Message
        error_message = {"message":str(e)}
        print(error_message)
            
    


      


        
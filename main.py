# Assignment 3 Project for Course BAN6420 (Programming in Python and R)
"""
Policy Management System for an Insurance Company

Task 0 : Class Creation: - Create separate classes for policyholders, products, and payments.
Task 1 : Policyholder Management: - Implement methods to register, suspend, and reactivate policyholders.
Task 2 : Payment Management: - Implement methods for payment processing, reminders, and penalties.
Task 3 : Product Management: - Implement methods for creating, updating, and removing/suspending policy products.
Task 4 : Policyholder Demonstration: - Create at least two policyholders who have paid for one of the products and display their account details.
"""


from models import policyholders, payments, products
from datetime import datetime


def main():

    # Error Handlig
    try:

        # Create a dictionary database to store the class objects
        payments_database = {}
        products_database = {}
        policy_holders_database = {}


        # Task 4 : Policyholder Demonstration: - Create at least two policyholders and store them in policy_holders_database
        policyholder_one = policyholders.PolicyHolder(fname="Onyedikachi", lname="Ezeobi", policy_number=2100100343, account_balance=10000)
        policyholder_one.register_policy_holder(policy_holders_database=policy_holders_database)

        policyholder_two = policyholders.PolicyHolder(fname="Ogechi", lname="Ezeobi", policy_number=3100100344, account_balance=20000)
        policyholder_two.register_policy_holder(policy_holders_database=policy_holders_database)


        # Creating three products and store them in products_database usinf product code as the key
        produt_one = products.Product(product_name="Health Issurance", product_code="HEI", price=1000)
        produt_one.create_product(products_database=products_database)
        
        product_two = products.Product(product_name="Travel Issurance", product_code="TRI", price=2000)
        product_two.create_product(products_database=products_database)

        product_three = products.Product(product_name="Life Issurance", product_code="LFI", price=3000)
        product_three.create_product(products_database=products_database)


        # Create payments for the products and store the product code as 'key' and list of the policy_holder's policy_number as the 'values'
        payment_one = payments.Payments(product=produt_one, policy_holder=policyholder_one, due_date=datetime.strptime("30/08/2024", "%d/%m/%Y").date())
        payment_one.processing_payment(payments_database=payments_database)

        payment_two = payments.Payments(product=produt_one, policy_holder=policyholder_two, due_date=datetime.strptime("30/09/2024", "%d/%m/%Y").date())
        payment_two.processing_payment(payments_database=payments_database)

        payment_three = payments.Payments(product=product_two, policy_holder=policyholder_one, due_date=datetime.strptime("30/09/2024", "%d/%m/%Y").date())
        payment_three.processing_payment(payments_database=payments_database)

        payment_four = payments.Payments(product=product_two, policy_holder=policyholder_two, due_date=datetime.strptime("30/09/2024", "%d/%m/%Y").date())
        payment_four.processing_payment(payments_database=payments_database)


        # Task 4 : Policyholder Demonstration: - Create at least two policyholders who have paid for one of the products and display their account details.
        policyholder_one.display_acct_details(payments_database=payments_database, products_database=products_database)
        policyholder_two.display_acct_details(payments_database=payments_database, products_database=products_database)
        payments.payment_reminders(payments_database)
    

    # Error Handling for Exception
    except Exception as e:
        # Error Message
        error_message = {"message":str(e)}
        print(error_message)


if __name__ == "__main__":
    main()


"""
Task 1 : Policyholder Management: - Implement methods to register, suspend, and reactivate policyholders.
"""

from json import dumps

class PolicyHolder:
    def __init__(self, fname, lname, policy_number, account_balance=0, status=True):
        self.fname = fname
        self.lname = lname
        self.policy_number = policy_number
        self.account_balance = account_balance
        self.status = status


    def register_policy_holder(self, policy_holders_database:dict):
        "*To register a new policy holder*"
        try:
            if not self.policy_number in policy_holders_database:
                policy_holders_database[self.policy_number] = self
                print(f"The account name {self.fname} {self.lname} has been registered successfully")
            else:
                print(f"Policy number {self.policy_number} already exist")

        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


    def suspend_policy_holder(self, policy_holders_database:dict):
        "*To suspend a policy holder*"

        try:
            if self.policy_number in policy_holders_database:
                self.status = False if self.status == True else print(f"The account is already suspended")
                print(f"The account {self.fname} {self.lname} has been suspended")
            else:
                print(f"Account number {self.policy_number} does not exist")
            
        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


    def reactivate_policy_holder(self, policy_holders_database:dict):
        "*To reactivate a policy holder*"

        try:
            if self.policy_number in policy_holders_database:
                self.status = True if self.status == False else print(f"The account is already active")
                print(f"The account {self.fname} {self.lname} has been reactivated")
            else:
                print(f"Account number {self.policy_number} does not exist")
            
        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


    def display_acct_details(self, payments_database:dict, products_database:dict):
        "*To display accounnt details*"

        try:
            # Status Code mapping
            status_code = {True:"Active", False:"Suspended"}

            # Fetch all the records for the policy-holder
            paid_products_code = [product_code for product_code, policy_holder_list in payments_database.items() if self.policy_number in policy_holder_list]

            # Retrieve the Product Details
            paid_products_name = [products_database.get(product_code).product_name for product_code in paid_products_code]

            # Policy Holder's Account Details
            account_details = {
                "Name of Policy Holder" : f"{self.fname} {self.lname}",
                "Policy Number" : self.policy_number,
                "Account Balance" : self.account_balance,
                "Account Status" : status_code.get(self.status),
                "Products" : paid_products_name
            }
            print(dumps(account_details, indent=4))

        # Error Handling for Exception
        except Exception as e:
            # Error Message
            error_message = {"message":str(e)}
            print(error_message)


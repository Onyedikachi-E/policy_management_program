# Module 3 Assignment (Milestone 1): Policy Management System for an Insurance Company 

This is a program is mangement application for Insurrance company where the program will manage the operations of the company. It will be able to register new policy-holders and manage their accounts and it will be able to register new products and manage it. Lastly the policy-holders will be able to purchase any products of their choice which will be mapped in the temp database.


## Key Features

- **Three temporary database**: I created three temporary dictionary to serve as database tables.
    - **Policy Holder Dictionary**: This table will store the policy-holder objects which has all the attributes and methods of the PolicyHolder class.

    - **Product Dictionary**: This table will store the product objects which has all the attributes and methods of the Product class.

    - **Payments Dictionary**: This is a nested dictionary that takes the product code as key and dictionary of policy holders that paid for it and payment objects as the value.

- **Class Creation on seperate files**: Three classes were created to serve as the blue print to their objects.

    - **PolicyHolder Class**: This is a special class to model the architecture design of the Policy Holders which are - (Account name, Policy number, Account balance, Account status). It also have define methods for certain actions.

    - **Product Class**: This is a special class to model the desiggn of the product objects. They include (Product name and Product Code). It also has defined methods for certian actions.

    - **Payments Class**: This is a special class to create the blue prints for the payments objects. It hass product and policy-holder object as attributes alongside other defined methods to perfom certain actions.

- **Error Handling**: Added Error Handling to track any exception and print the error as a string or character.

- **Lanuguage Stack**: The Policy Management Program was written using Python.

- **Normalization**: The dictionary database was well normalized to avoid data redundancy in each of the dictionary and did a look up to each dictionary to query certain data. Records were stored using key - value pair and can easily be retrieved.

- **Documentation Strings**: This type of documentation was done to easily give highlight to what action each of the methods performs.

- **Encapsulation**: This class concept was utilized in such a way the objects of class are instantiated and wrapped with attributes and methods of that class to perform tasks.



## GitHub Repository

- **GitHub**: Added the project to Github - https://github.com/Onyedikachi-E/policy_management_program

## Packages Used in the project

1. **json** - This package was used to pretty print the Employee details using indentation 4.
2. **datatime** - This package was used to invoke current date using .now() method.

## How To Use The Program

1. Install the json package -- "pip install json"
2. Execute the "main.py" file on the terminal to display the account details of two of the Policy-Holder. -- "python3 main.py"

"""
Module: utils_lis

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my spring 2025 semester
analytics projects. The purpose is to create and get comfortable with code.
We want our code to be reusable. A good byline can be used in every Python 
analytics project we do this semester. 

Author: Lisete Sax

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True
is_locally_grown: bool = True
is_organic: bool = True
has_membership_discount = True
has_return_options = True
has_student_discount = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 22
years_in_global_operations = 5

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.9
average_delivery_time: float = 4.4
coffee_bean_variety: float = 4.8
customer_service_communication= 4.9

# declare a list of strings
# TODO: Add or replace this with your own list  
products_offered: list = ["Espresso Beans", "Flavor Syrup", "Organic Coffee"]
available_merchandise: list = ["Coffee Cups", "Gift Cards", "T-Shirts"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
client_delivery_scores: list = [4.9, 4.4, 5.0, 4.8]
coffee_taste_score: list = [5.0, 4.8, 4.2, 4.6]
customer_service_score: list = [4.9, 4.9, 5.0, 4.7, 5.0] 

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)
min_score: float = min(client_delivery_scores)  
max_score: float = max(client_delivery_scores)  
mean_score: float = statistics.mean(client_delivery_scores)  
stdev_score: float = statistics.stdev(client_delivery_scores)
min_score: float = min(coffee_taste_score)  
max_score: float = max(coffee_taste_score)  
mean_score: float = statistics.mean(coffee_taste_score)  
stdev_score: float = statistics.stdev(coffee_taste_score)
min_score: float = min(customer_service_score)  
max_score: float = max(customer_service_score)  
mean_score: float = statistics.mean(customer_service_score)  
stdev_score: float = statistics.stdev(customer_service_score)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Blue Ridge Coffee: Delivering Coffee Worldwide
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
years_in_global_operations: {years_in_global_operations}
Products Offered:           {products_offered}
Available Merchandise:      {available_merchandise}       
Client Satisfaction Scores: {client_satisfaction_scores}
Client Delivery Scores:     {client_delivery_scores}
Coffee Taste Score:         {coffee_taste_score}
Customer Service Score:     {customer_service_score}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.

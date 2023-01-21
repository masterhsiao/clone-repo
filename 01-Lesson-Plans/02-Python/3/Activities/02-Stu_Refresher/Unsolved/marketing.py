# -*- coding: utf-8 -*-
"""Refresher activity.

This script will use variables, conditionals, lists, dicts, and functions
to print out different greetings for customers based on their
business tier (determined by revenue).
"""

# List of dicts
customers = [
    { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
    { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
    { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
    { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
]

# @TODO Define a function that accepts a customer first_name, last_name, and
# revenue and returns a custom greeting with the full name.
# Use these ranges to determine the business tier (and corresponding message)
# for each customer.
#   Platinum = 3001+
#   Gold = 2001-3000
#   Silver = 1001-2000
#   Bronze = 0-1000
def create_greeting(first_name, last_name, revenue):
    if revenue >= 3001:
        return f"Dear {first_name} {last_name}, as a Platinum customer, we wanted to express our sincere gratitude for your loyalty and support. We value your business and look forward to serving you for many years to come."
    elif revenue >= 2001:
        return f"Dear {first_name} {last_name}, as a Gold customer, we appreciate your continued support and look forward to providing you with excellent service. Thank you for choosing us."
    elif revenue >= 1001:
        return f"Dear {first_name} {last_name}, as a Silver customer, we value your business and look forward to serving you. Thank you for choosing us."
    else:
        return f"Dear {first_name} {last_name}, as a Bronze customer, we appreciate your business and hope to serve you again in the future. Thank you for choosing us."

for customer in customers:
    first_name = customer["first_name"]
    last_name = customer["last_name"]
    revenue = customer["revenue"]
    greeting = create_greeting(first_name, last_name, revenue)
    print(greeting)

# @TODO: Loop through the list of customers and use your function to print
# custom greetings for each customer.
# @TODO: YOUR CODE HERE!

# Import things
from art import logo

import sys, time

# from replit import clear

power = True
question = "no"
result = 0
# Print logo
print(logo)


# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


def all_symbols():
    for symbol in operations:
        print(symbol)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Calculator
def calculator():
    # Questions for user numbers
    num1 = float(input("What's the first number?: "))
    all_symbols()  # For loop to show all symbols
    power = True

    while power:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, press 'enter' to start new calculation: ") == "y":
            num1 = answer
        else:
            power = False
            calculator()


calculator()

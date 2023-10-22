# Бібліотека калькулятора
# calculator_library.py

import math
import logging

logging.basicConfig(filename='calc.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not allowed")
    return math.sqrt(x)

def validate_operator(operator):
    valid_operators = ['+', '-', '*', '/', '**', 'sqrt']
    return operator in valid_operators

def safe_operation(operator, x, y=None):
    try:
        if operator == 'sqrt':
            if x < 0:
                raise ValueError("Square root of a negative number is not allowed")
            result = square_root(x)
        elif operator in {'+', '-', '*', '/', '**'}:
            result = eval(f"{x}{operator}{y}")
        else:
            raise ValueError("Invalid operator")
        logging.info(f"Operation: {x} {operator} {y if y is not None else ''} = {result}")
        return result
    except Exception as e:
        logging.error(f"Error: {e}")
        
def validate_operator(operator):
    valid_operators = ['+', '-', '*', '/', '**', 'sqrt']
    return operator in valid_operators

def genFloatValue(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

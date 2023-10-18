# Бібліотека калькулятора
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
    return x ** 0.5

def validate_operator(operator):
    valid_operators = ['+', '-', '*', '/', '**', 'sqrt']
    return operator in valid_operators

def genFloatValue(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def safe_operation(operator, x, y):
    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)
    elif operator == '**':
        return power(x, y)
    elif operator == 'sqrt':
        return square_root(x)
    else:
        raise ValueError("Invalid operator")

def handle_input(operator, n1, n2):
    if operator in ['+', '-', '*', '/', '**']:
        return safe_operation(operator, n1, n2)
    elif operator == 'sqrt':
        return safe_operation(operator, n1)
    else:
        raise ValueError("Invalid operator")

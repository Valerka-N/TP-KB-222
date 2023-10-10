def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result = x / y
        return result
    except ZeroDivisionError as e:
        return str(e)

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not allowed")
    return x ** 0.5

def validate_operator(operator):
    valid_operators = ['+', '-', '*', '/', '**', 'sqrt']
    return operator in valid_operators

while True:
    print("Make a feature selection:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. **")
    print("6. Square root extraction")
    print("7. Exit")

    choice = input("Enter the operator of the function to perform (+/-/*///**): ")

    if choice == '7':
        print("Exiting the calculator.")
        break

    if not validate_operator(choice):
        print("Invalid operator. Please choose a valid operator.")
        continue

    try:
        n1 = float(input("First number: "))
        result = None

        if choice in ['+', '-', '*', '/', '**']:
            n2 = float(input("Second number: "))

            if choice == '+':
                result = add(n1, n2)
            elif choice == '-':
                result = subtract(n1, n2)
            elif choice == '*':
                result = multiply(n1, n2)
            elif choice == '/':
                result = divide(n1, n2)
            elif choice == '**':
                result = power(n1, n2)

        elif choice == 'sqrt':
            result = square_root(n1)

        print("Result:", result)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

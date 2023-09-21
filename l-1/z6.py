def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "error"
    return x / y
def power(x, y):
    return x ** y
def square_root(x):
    if x < 0:
        return "error"
    return x ** 0.5

while True:
    print("make a feature selection:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. **")
    print("6. Square root extraction")
    print("7. exit")

    choice = input(" enter the number of the function to perform (1/2/3/4/5/6/7): ")

    match choice:
        case '1':
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            result = add(n1, n2)
        case '2':
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            result = subtract(n1, n2)
        case '3':
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            result = multiply(n1, n2)
        case '4':
            n1 = float(input("First number: "))
            n2 = float(input("Second number: "))
            result = divide(n1, n2)
        case '5':
            n1 = float(input("base: "))
            n2 = float(input("exponent: "))
            result = power(n1, n2)
        case '6':
            n1 = float(input("number: "))
            result = square_root(n1)
        case '7':
            print("exit")
            break
        case _:
            print("error")
            continue

    print("result:", result)

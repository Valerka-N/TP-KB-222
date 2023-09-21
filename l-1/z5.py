import math

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
    return math.sqrt(x)

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

    if choice == '7':
        print("exit")
        break

    if choice not in ('1', '2', '3', '4', '5', '6'):
        print("error")
        continue

    if choice in ('1', '2', '3', '4', '5'):
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))

    if choice == '1':
        print("result:", add(n1, n2))

    elif choice == '2':
        print("result:", subtract(n1, n2))

    elif choice == '3':
        print("result:", multiply(n1, n2))

    elif choice == '4':
        print("result:", divide(n1, n2))

    elif choice == '5':
        print("result:", power(n1, n2))

    elif choice == '6':
        n3 = float(input("number: "))
        print("result:", square_root(n3))
        

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def infix_to_rpn(expression):
    output = []
    stack = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and is_operator(stack[-1]) and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_rpn(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(float(char))
        elif is_operator(char):
            n2 = stack.pop()
            n1 = stack.pop()
            if char == '+':
                stack.append(n1 + n2)
            elif char == '-':
                stack.append(n1 - n2)
            elif char == '*':
                stack.append(n1 * n2)
            elif char == '/':
                stack.append(n1 / n2)
    return stack[0]

if __name__ == "__main__":
    inpt = input("Введіть вираз: ")
    rpn_expression = infix_to_rpn(inpt)
    print("Вираз у ЗПН:", ''.join(rpn_expression))
    result = evaluate_rpn(rpn_expression)
    print("Результат:", result)

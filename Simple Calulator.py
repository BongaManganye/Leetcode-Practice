#Simple Calulator

#Write a program that takes two numbers and an operator (+, -, *, /) as inputs the calculated results.
#Handle division by zero gracefully.

def calc(n1, n2, op):
    if op == '+' : return n1 + n2
    elif op == '-' : return n1 - n2
    elif op == '*' : return n1 * n2
    elif op == '/' : return n1 / n2 if n2 != 0 else "Error: Division by zero"
    return "Invalid opertor"

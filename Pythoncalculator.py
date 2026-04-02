# Simple Python Calculator by Amanam Matthew

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("A Simple Python Calculator Program ")
print("Operations: +  -  *  /")

while True:
    choice = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")

    if choice == 'q':
        print("Calculator closed.")
        break

    if choice not in ['+', '-', '*', '/']:
        print("Invalid operation.")
        continue

    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("Invalid number.")
        continue

    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", subtract(num1, num2))
    elif choice == '*':
        print("Result:", multiply(num1, num2))
    elif choice == '/':
        print("Result:", divide(num1, num2))
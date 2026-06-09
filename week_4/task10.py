def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a,b):
    return a**b

def modulas(a,b):
    return a%b

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, **, %): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(add(num1, num2))

elif operator == "-":
     print(subtract(num1, num2))

elif operator == "*":
    print(multiply(num1, num2))

elif operator == "/":
    print(divide(num1, num2))

elif operator == "**":
    print(power(num1, num2))

elif operator == "%":
    print(modulas(num1, num2))

else:
    print("Invalid operator")
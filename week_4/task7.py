def is_greater(a,b,c):
    if a > b and a > c:
        return "a is greater"
    elif b > a and b > c:
        return "b is greater"
    else: 
        return "c is greater"


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

d = is_greater(num1, num2, num3)
print(d)
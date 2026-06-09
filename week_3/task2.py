greater_number = lambda x,y: x if x > y else y
def table(b,a): 
    number = b
    for i in range(1, a+1):
        print(f"{number} x {i} = {number * i}")
first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))
range_limit = int(input("Enter the range for multiplication table: "))
bigger_number =greater_number(first_number, second_number)
table(bigger_number, range_limit)
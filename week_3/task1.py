import math
print("The formula of permutation is P(n,r)=n!/(n-r)!​, and formula of combination is C(n,r)=n!/r!(n-r)!​")
def factorial_function(user_input,user_input_r):
    if user_input == 0 or user_input == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, user_input + 1):
            factorial *= i
        return factorial

def permutation_function(user_input, user_input_r):
    return factorial_function(user_input, user_input_r) // factorial_function(user_input - user_input_r, user_input_r)

def combination_function(user_input, user_input_r):
    return factorial_function(user_input, user_input_r) // factorial_function(user_input_r, user_input_r) // factorial_function(user_input - user_input_r, user_input_r)

user_input = int(input("Enter a the value of n: "))
user_input_r = int(input("Enter a the value of r: "))
factorial = factorial_function(user_input, user_input_r)
permutation = permutation_function(user_input, user_input_r)
combination = combination_function(user_input, user_input_r)
print(f"The factorial of the {user_input} is {factorial}")
print(f"The permutation of the {user_input} taken {user_input_r} at a time is {permutation}")
print(f"The combination of the {user_input} taken {user_input_r} at a time is {combination}")

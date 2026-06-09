# Variant A - academic edition
number = int(input("Enter a decimal number: "))
power = 0
binary_number = 0
while number > 0:
    last_digit = number %2
    binary_number += last_digit * (10 ** power)
    power += 1
    number //= 2
print("Binary number is: ", binary_number)
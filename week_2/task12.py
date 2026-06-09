# Variant A - academic edition
import math
binary_number = (input("Enter a binary number: "))
decimal_number = 0
exponent = 0
binary_output = 0
for digit in str(binary_number)[::-1]:
    if digit == '1' or digit == '0':
        decimal_number += int(digit) * (2 ** exponent)
    elif digit != '1' and digit != '0':
        print("Invalid binary number")
        break
    exponent += 1
print("Decimal number is: ", decimal_number)

for digit in str(decimal_number)[::-1]:
    binary_output += (int(digit) % 2) * (10 ** exponent)
    decimal_number //= 2
    exponent += 1
print("Binary number is: ", binary_output)
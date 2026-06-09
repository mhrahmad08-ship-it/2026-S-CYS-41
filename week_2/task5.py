# Variant A - academic edition
number = int(input("Enter a binary number: "))
decimal_number = 0
power = 0
while number > 0:
    last_digit = number % 10
    decimal_number += last_digit * (2 ** power)
    power += 1
    number //= 10
print("Decimal number is: ", decimal_number)
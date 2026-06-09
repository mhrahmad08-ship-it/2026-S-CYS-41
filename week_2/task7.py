# Variant A - academic edition
import math
first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))
sum_of_prime_numbers = 0
if second_number < first_number:
    minimum = second_number
    maximum = first_number

for number in range(minimum, maximum + 1):
    if number > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(number)) +1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number, " is a prime number")
            sum_of_prime_numbers += number
print("Sum of prime numbers between ", first_number, " and ", second_number, " is: ", sum_of_prime_numbers)
 
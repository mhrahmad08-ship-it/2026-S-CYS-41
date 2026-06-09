# Variant A - academic edition
import random
for i in range(15, 21, 2):
    print("Number is: ", i)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password_length = int(input("Enter the length of the password: "))
password = ""
for i in range(password_length):
        password += random.choice(chars)
print("Generated password: ", password)
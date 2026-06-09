# Variant A - academic edition
import random
import string
length = int(input("Enter the length of the password: "))
uppercase_letters = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase_letters = input("Include lowercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
special_characters = input("Include special characters? (y/n): ").lower() == 'y'
character_pool = ""
if uppercase_letters:
    character_pool += string.ascii_uppercase
if lowercase_letters:
    character_pool += string.ascii_lowercase
if digits:
    character_pool += string.digits
if special_characters:
    character_pool += string.punctuation
if not character_pool:
    print("No character types selected. Please select at least one type.")
else:
    password = ''.join(random.choice(character_pool) for _ in range(length))
    print("Generated password: ", password)
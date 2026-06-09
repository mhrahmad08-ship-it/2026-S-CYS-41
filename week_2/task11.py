# Variant A - academic edition
import string
user_input = input("Enter a string: ")
vowel_chars = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0
for char in user_input:
    if char.lower() in vowel_chars:
        vowel_count +=1
    elif char.isalpha():
        consonant_count +=1
    elif char == " ":
        continue
    elif char in string.punctuation:
        continue
print("Number of vowels: ", vowel_count)
print("Number of consonants: ", consonant_count)
for char in user_input:
    percentage = (vowel_count / len(user_input)) * 100 
print("Percentage of vowels: ", percentage, "%")
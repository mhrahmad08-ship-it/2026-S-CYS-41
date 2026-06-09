# Variant A - academic edition
str = input("Enter your String: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_counter = 0
consonant_counter = 0

for letter in str:
    if letter in vowels:
        vowel_counter += 1
    elif letter not in vowels and letter.isalpha():
        consonant_counter += 1


print("Vowels in string are: ", vowel_counter,"  Consonants in string are: ", consonant_counter)
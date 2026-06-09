upper_case = lambda s:s.upper()
def reverse_string(existing_string):
    for i in range (len(existing_string) - 1, -1, -1): 
        print(existing_string[i], end='')
        
user_input = input("Enter a string: ")
user_string = upper_case(user_input)
reverse_string(user_string)
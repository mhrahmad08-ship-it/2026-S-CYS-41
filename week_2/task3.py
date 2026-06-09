# Variant A - academic edition
password = "password"
user_name = "Administrator"
max_attempts = 5
atemp = 0

while atemp < max_attempts:
    user_password = input("Enter user password: ")
    if user_password == password:
        print("Welcome " + user_name)
        break
    else:
        atemp += 1
        print("Wrong password")

    if(atemp == max_attempts):
        print("Too many attempts")
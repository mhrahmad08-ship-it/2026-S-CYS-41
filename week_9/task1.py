# Variant A - academic edition
for i in range(1, 11):
    for j in range(1, 5):
        print(i*j , end = "\t" )
    print()

for i in range(1,4):
    for j in range(2,4):
        print(f"{i} and {j}")

for i in range(1, 5):
    for j in range(1, i+1):
        print("*", end="")        
    print()

stars = 5
for i in range(stars):
    spaces = stars - i - 1
    print('' * spaces + '*' * (2*i + 1))

stars = 5 
for i in range(stars):
    for space in range(stars - i -1):
        print('  ', end = '')
    for star in range(2*i+1):
        print("*", end = ' ')
    print()
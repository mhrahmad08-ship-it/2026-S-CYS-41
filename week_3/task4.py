def celesius_to_fahrenheit(cel):
    return (cel * 9/5) + 32

def fahrenheit_to_celesius(far):
    return (far - 32) * 5/9

celesius = float(input("Enter Celsius: "))
fahrenheit = float(input("Enter Fahrenheit: "))
celes_to_fahren = celesius_to_fahrenheit(celesius)
fahren_to_celes = fahrenheit_to_celesius(fahrenheit)
print(f"the value of celesius in fahrenheit is {celes_to_fahren}")
print(f"the value of fahrenheit in celesius is {fahren_to_celes}")
def power(base, exponent = 2):
    return base ** exponent


base = int(input("Enter a base number: "))
exponent = input("Enter the exponent: ")
if exponent == "":
    raised = power(base)
else:
    raised = power(base,int(exponent))
print(raised)
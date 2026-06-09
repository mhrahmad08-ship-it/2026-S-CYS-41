def total(*numbers):
    sum_of_numbers = 0

    for i in numbers:
        sum_of_numbers += i
    
    print("Total: ",sum_of_numbers )

total(5,6,7,8,9)
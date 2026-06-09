def avg(*numbers):
    sum_of_numbers = 0

    for i in numbers:
        sum_of_numbers += i

    average = sum_of_numbers / len(numbers)
    print(f"the average of {numbers} is {average}")

avg(1,3,2,4)
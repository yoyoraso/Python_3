def sum_and_avg_of_int_numbers(num):
    if (num == 0):
        return num
    else:
        return (num * (num + 1) / 2)
number = int(input("Please Enter any Number: "))
total = sum_and_avg_of_int_numbers(number)
average = total / number
print("The Sum of int Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of int Numbers from 1 to {0} =  {1}".format(number, average))
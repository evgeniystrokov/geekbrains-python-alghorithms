#7. Напишите программу, доказывающую или проверяющую,
#что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input("Please, enter n \n"))

next_element = 1
sequence_sum_right = n * (n + 1) / 2
sequence_sum_left = 0

for i in range(n):
    sequence_sum_left += next_element
    next_element += 1

if sequence_sum_left == sequence_sum_right:
    print("Success, equality confirmed")
else:
    print("Failure, sides are not equal")

#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

MAX_INT = 100
LIST_SIZE = 10

random_numbers = [random.randrange(MAX_INT) for _ in range(LIST_SIZE)]

min_number = MAX_INT + 1
min_index = -1
max_number = -1
max_index = -1

print(random_numbers)

for i in range(LIST_SIZE):
    if random_numbers[i] > max_number:
        max_number = random_numbers[i]
        max_index = i

    if random_numbers[i] < min_number:
        min_number = random_numbers[i]
        min_index = i


numbers_sum = 0

if min_index > max_index + 2:
    sum_start = max_index + 1
    sum_end = min_index
elif max_index > min_index + 2:
    sum_start = min_index + 1
    sum_end = max_index
else:
    sum_start = -1
    sum_end = -1
    
if sum_end > 0:
    for i in range(sum_start, sum_end):
        print(random_numbers[i])
        numbers_sum += random_numbers[i]
    

print(numbers_sum)

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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


random_numbers[min_index] = max_number
random_numbers[max_index] = min_number

print(random_numbers)

    

#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

LIST_SIZE = 100
MAX_INT = 100

numbers_list = [random.randrange(-MAX_INT, MAX_INT) for _ in range(LIST_SIZE)]

max_negative = -MAX_INT - 1

print(numbers_list)

for i in range(LIST_SIZE):
    if numbers_list[i] < 0 and numbers_list[i] > max_negative:
        max_negative = numbers_list[i]

print(max_negative)

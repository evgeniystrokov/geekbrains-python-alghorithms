#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

MAX_INT = 100
COLUMN_COUNT = 5
ROW_COUNT = 5

numbers_matrix = [[random.randrange(MAX_INT) for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)] 

for i in range(ROW_COUNT):
    print(numbers_matrix[i])

max_element = -1

for j in range(COLUMN_COUNT):
    min_element = numbers_matrix[0][j]

    for i in range(1, ROW_COUNT):
        if numbers_matrix[i][j] < min_element:
            min_element = numbers_matrix[i][j]


    if min_element > max_element:
        max_element = min_element

print(max_element)

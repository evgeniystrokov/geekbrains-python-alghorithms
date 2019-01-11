#4. Определить, какое число в массиве встречается чаще всего.
import random

LIST_SIZE = 100
MAX_INT = 10

numbers_list = [random.randrange(MAX_INT) for _ in range(LIST_SIZE)]

most_frequent_number = -1
max_frequency = 0

for i in range(LIST_SIZE):
    frequency = 0

    for j in range(LIST_SIZE):
        if numbers_list[i] == numbers_list[j]:
            frequency += 1

    if frequency > max_frequency:
        most_frequent_number = numbers_list[i]
        max_frequency = frequency


print(numbers_list)
print(most_frequent_number, max_frequency)

#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#Количество элементов (n) вводится с клавиатуры.

n = int(input("Please, enter n \n"))

next_element = 1
sequence_sum = 0

for i in range(n):
    sequence_sum += next_element
    next_element *= -0.5

print(f"The result is {sequence_sum}")

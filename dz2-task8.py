#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

digit = input("Please, enter the digit to count\n")

number_count = int(input("Please, enter the number of numbers to analyze\n"))

result = 0

for i in range(number_count):
    next_number = input("Please, enter next number\n")
    result += next_number.count(digit)

print(f"Digit {digit} was found {result} times in the numbers provided")

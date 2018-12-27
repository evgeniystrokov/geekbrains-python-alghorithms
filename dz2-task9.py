#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#Вывести на экран это число и сумму его цифр.

def digits_sum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10

    return sum

number_count = int(input("Please, enter number of numbers to analyze\n"))

leader = 0
leader_digits_sum = 0

for i in range(number_count):
    next_number = int(input("Please, enter your next number\n"))

    next_number_digits_sum = digits_sum(next_number)

    if next_number_digits_sum > leader_digits_sum:
        leader = next_number
        leader_digits_sum = next_number_digits_sum

print(f"Greatest digits sum was {leader_digits_sum} for number {leader}")

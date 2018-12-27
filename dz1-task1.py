#Евгений Строков
#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

input_string = input("Hi, please, enter a 3-digit number. Type 'exit' to exit the program.\n")
while True:
    if input_string == 'exit':
        break
    try:
        number = int(input_string)
        if number > 99 and number < 1000:
            a = number // 100
            b = number // 10 - 10 * a
            c = number % 10
            print("Sum of the digits is: ", (a + b + c))
            print("Product of the digits is: ", (a * b * c))
            input_string = input("Enter next 3-digit number or type 'exit' to exit the program.\n")
        else:
            input_string = input("The number provided is not valid, please, try again! Type 'exit' to exit the program.\n")
    except ValueError:
        input_string = input("Wrong imput, try again, please! Type 'exit' to exit the program.\n")


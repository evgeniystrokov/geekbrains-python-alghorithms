#Евгений Строков
"""4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""

import random, string
from datetime import datetime

print("Hi, this generates random numbers or characters within specified range. Float coordinates supported.")
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    try:
        random.seed(datetime.now())
        print("...")
        input_string = input("Please, choose mode. Type i for integers, f for floats or c for characters. Type 'exit' to exit the program.\n")
        if input_string == 'exit':
            break
        elif input_string == "i":
            input_string = input("Please, enter first border for the generator interval.\n")
            a = int(input_string)

            input_string = input("Please, enter second border for the generator interval.\n")
            b = int(input_string)
            
            if a > b:
                print("Random integer:", random.randint(b, a))
            elif b > a:
                print("Random integer:", random.randint(a, b))
            else:
                print("Borders are equal to each other. The only option is:", a)
                
        elif input_string == "f":
            input_string = input("Please, enter first border for the generator interval.\n")
            a = float(input_string)

            input_string = input("Please, enter second border for the generator interval.\n")
            b = float(input_string)

            if a > b:
                print("Random float:", random.uniform(b, a))
            elif b > a:
                print("Random float:", random.uniform(a, b))
            else:
                print("Borders are equal to each other. The only option is:", a)
                
        elif input_string == "c":
            print("For this mode we use the following char range:", ALPHABET)
            first_char = input("Please, enter first border for the generator interval.\n")
            second_char = input("Please, enter second border for the generator interval.\n")

            a = ALPHABET.find(first_char)
            b = ALPHABET.find(second_char)
            if len(first_char) == 1 and len(second_char) == 1 and (a * b) >= 0:
                if a > b:
                    print("Random character:", random.choice(ALPHABET[b:a]))
                elif b > a:
                    print("Random character:", random.choice(ALPHABET[a:b]))
                else:
                    print("Borders are equal to each other. The only option is:", ALPHABET[a])    
            else:
                print("Incorrect input, please, try again.")
        else:
            print("Incorrect mode, please, try again.")
        
    except ValueError:
        print("Wrong input, try again, please! Type 'exit' to exit the program.")

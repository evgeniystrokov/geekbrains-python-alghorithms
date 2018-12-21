#Евгений Строков
#3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

print("Hi, this programm takes 2 points as input and calculates line equation. Float coordinates supported.")
while True:
    try:
        print("...")
        input_string = input("Please, enter x1. Type 'exit' to exit the program.\n")
        if input_string == 'exit':
            break
        x1 = float(input_string)

        input_string = input("Please, enter y1. Type 'exit' to exit the program.\n")
        if input_string == 'exit':
            break
        y1 = float(input_string)

        input_string = input("Please, enter x2. Type 'exit' to exit the program.\n")
        if input_string == 'exit':
            break
        x2 = float(input_string)

        input_string = input("Please, enter y2. Type 'exit' to exit the program.\n")
        if input_string == 'exit':
            break
        y2 = float(input_string) 
            
        print("First point: (", x1, ", ", y1, ")")
        print("Second point: (", x2, ", ", y2, ")")

        if x1 == x2:
            if y1 == y2:
                print("Can't determine line equation because x1 == x2 and y1 == y2. Please, try again and enter different coordinates.")
            else:
                print("Line equation is: x = ", x1)
        elif y1 == y2:
            print("Line equation is: y = ", y1)
        else:
            k = (y2 - y1)/(x2 - x1)
            b = x1 * (y2 - y1) / (x1 - x2) + y1
            print("Line equation is: y = ", k, "* x +", b)
    except ValueError:
        print("Wrong input, try again, please! Type 'exit' to exit the program.")

#2. Посчитать четные и нечетные цифры введенного натурального числа.
#Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def calc_digits(number, residue):
    if number > 9:
        return ((number % 2) == residue) + calc_digits(number // 10, residue)
    else:
        return ((number % 2) == residue)

number = int(input("Please, enter your number\n"))

odd_digits = calc_digits(number, 1)
even_digits = calc_digits(number, 0)

print(f"There are {odd_digits} odd digits and {even_digits} even digits in your number")

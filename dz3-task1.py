#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

scope = range(2, 100)
dividers = range(2, 10)
results = [0] * 8

for i in range(len(scope)):
    for j in range(len(dividers)):
        results[j] += (scope[i] % dividers[j] == 0)

print(results)
    

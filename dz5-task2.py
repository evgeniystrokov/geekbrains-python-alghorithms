from collections import Counter
from collections import deque

BASE = 16 #up to 36
DIGITS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
          "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y" "Z")

def toStr(n, base):
   if n < base:
      return DIGITS[n]
   else:
      return toStr(n // base, base) + DIGITS[n % base]

operand = input("Please, enter operation to perform: + or *\n")

first_input = input("Please, enter the first number\n")
first_number = Counter()
pos = 1
for char in reversed(first_input):
    first_number[pos] = DIGITS.index(char.upper())
    pos *= BASE

second_input = input("Please, enter the second number\n")
second_number = Counter()
pos = 1
for char in reversed(second_input):
    second_number[pos] = DIGITS.index(char.upper())
    pos *= BASE

if operand == "+":
    check = toStr(int(first_input, BASE) + int(second_input, BASE), BASE)
    result = first_number + second_number
else:
    check = toStr(int(first_input, BASE) * int(second_input, BASE), BASE)
    result = Counter()
    first_pos = 1
    for i in range(len(first_number)):
        second_pos = 1
        for j in range(len(second_number)):
            result[first_pos * second_pos] += first_number[first_pos] * second_number[second_pos]
            second_pos *= BASE
        first_pos *= BASE

while (result.most_common(1)[0][1]) >= BASE:
    pos, overflow = result.most_common(1)[0]
    result[pos * BASE] += overflow // BASE
    result[pos] = overflow % BASE

result_deque = deque()
pos = 1
for i in range(len(result)):
    result_deque.appendleft(DIGITS[result[pos]])
    pos *= BASE

print("My result is", "".join(result_deque))
print("Correct result should be", check)

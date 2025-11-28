#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = 1
if number < 0:
    k *= -1
lg = abs(number) % 10
if lg * k < 6 and lg != 0:
    print(f"Last digit of {number} is {lg * k} and is less than 6 and not 0")
elif lg == 0:
    print(f"Last digit of {number} is {lg} and is 0")
else:
    print(f"Last digit of {number} is {lg * k} and is greater than 5")


#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
unsigned_digit = abs(number) % 10
lastdigit = 0
if number < 0:
    lastdigit = -unsigned_digit
else:
    lastdigit = unsigned_digit
if number < 6:
    print(f"Last digit of {number:d} is {lastdigit} and is less than 6 and not 0")
elif number > 5:
    print(f"Last digit of {number:d} is {lastdigit} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {lastdigit} and is 0")

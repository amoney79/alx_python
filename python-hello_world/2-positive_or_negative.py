#!/usr/bin/env python3
from random import randint

number = randint(-10, 10)  # Assign a random signed number to the variable number

# Check if the number is positive, negative, or zero
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")


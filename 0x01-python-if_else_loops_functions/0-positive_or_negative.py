#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # Assigns a random signed number to the variable "number"

print(number, end=" ")

if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")

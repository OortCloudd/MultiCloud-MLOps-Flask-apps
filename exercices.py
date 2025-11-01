#!/usr/bin/env python3
from random import choices

def add (x, y):
    print(f"inside add function: {x} + {y}")
    return x + y

print("outside add function")

numbers = range(1, 1000)
for num in numbers:
    xx=choices(numbers)[0]
    yy=choices(numbers)[0]
    print(add(xx,yy))

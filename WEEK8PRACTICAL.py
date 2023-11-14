#!/usr/bin/env python 3

def aofrec():
    height = float(input("What is the height of the rectangle"))
    width = float(input("What is the height of the rectangle"))
    area = height * width
    print(f"The area of a rectangle with the height of {height} and the width of {width} the total area would be {area:.3f}")
    return ()

def alignment():
    name = input("Input a name")
    age = input("What is your age")
    print(f"{name:>15} - {age:10}")
    print(f"{name:^15} - {age:^10}")
    print(f"{name:>15} - {age:>10}")
    print(f"{name:15} - {age:#^5}")
    return()
alignment()

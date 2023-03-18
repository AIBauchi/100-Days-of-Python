#Write a Python script that calculates the area of a circle with user input
from math import pow,pi
radius = int (input("Please enter the radius of the circle: "))
area = pi * pow(radius,2)
print(f"The area of the circle is {area}")

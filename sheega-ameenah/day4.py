#Write a Python script that calculates the area of a circle with user input
import math
r = int (input("Please enter the radius of the circle: "))
Area = math.pi * pow(r,2)
print(f"The area of the circle is {Area}")

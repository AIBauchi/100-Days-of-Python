# Write a Python script that sorts a list of integers with user input
numbers = input("Please enter a list of numbers, seperated by spaces: \n").strip().split(' ')
numbers = [float(n) for n in numbers]
numbers.sort()
print (numbers)

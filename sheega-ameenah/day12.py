#Write a Python script that calculates the sum of all the elements in a list with user input.

elements = input("please enter the elements you want to sum up, make sure to give space inbetween them: \n")

liist = elements.split()

liist = [float(i) for i in liist]

total = sum(liist)

print("The sum of the elements is:", total)

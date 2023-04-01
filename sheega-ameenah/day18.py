#Write a Python script that finds the most frequent element in a list with user input.
from statistics import mode
user_list = input("please enter the list of numbers or words you want to check, seperated by spaces: \n").split(" ")
most_frequent = mode(user_list)
print(f"The most frequent element in this list is {most_frequent}")

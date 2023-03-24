# Write a Python script that checks if a string is a palindrome with user input.
# A string is said to be palindrome if it remains the same on reading from both ends. It means that when you reverse a given string, it should be the same as the original string.
def convert(string):
    lisst = []
    lisst[:0] = string
    return lisst

word = str(input("Hello , please enter the word you wish to check \n"))
initial_string =convert(word)
#inverse_string = initial_string.reverse()

inverse_string = initial_string[::-1]


if initial_string == inverse_string:
    print(f"The word {word} is a palindrome")
else:
    print(f"The word {word} is not a palindrome")






















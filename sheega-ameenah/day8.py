# Write a Python script that generates a random number between 1 and 100 and asks the user to guess it.
import random
number = int (input("Guess a number between 1 to 100 "))
answer = int(random.randrange(1,100))
while answer != number:
    if number > answer:
        answer = int(input(" Wrong, guess lower"))
    elif number < answer:
        answer = int(input(" Wrong, guess higher"))
    else:
        break
    
print("congratulations you got it right")    
    

        

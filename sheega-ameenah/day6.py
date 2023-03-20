#Write a Python script that calculates the factorial of a number with user input
print
number = int(input("please enter any number of your choice "))
factorial = 1
if number ==0:
    print("The factorial of 0 is 1")
elif number < 0:
        print("invalid input, please enter a positive number")
else:
        for i in range (1,number +1):
            factorial = factorial* i
        print(f" The {number}! = {factorial}")
            
    

# Write a Python script that checks if a number is prime with user input
a = int (input("please enter a number: ") )
if a> 1:
    for i in range(2, int(a/2)+1):
        if (a % i) == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")
else:
    print(n, "is not a prime number")

    


    
           

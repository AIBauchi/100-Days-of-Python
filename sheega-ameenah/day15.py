# Write a Python script that searches for a specific value in a list with user input

list_of_things = input('please enter a list of values seperated by space \n'). split(" ")
value = input('please enter the value you wish to search for \n')
for i in list_of_things:
    
    if i is value:
        print(f'{value} is part of the list')
        break
else:
    print(f'{value} is not part of the list')
    
        

print('Thank you')


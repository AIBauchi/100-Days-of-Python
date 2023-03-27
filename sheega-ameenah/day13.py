numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to numbers
numbers = [float(num) for num in numbers]

# Find the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# Print the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)

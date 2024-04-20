# Define a function to square a number
def square(x):
    return x ** 2

# Define the list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() function to square each element of the list
squared_numbers = list(map(square, numbers))

# Print the original and squared lists
print("Original List:", numbers)
print("Squared List:", squared_numbers)
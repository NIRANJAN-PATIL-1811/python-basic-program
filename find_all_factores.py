def find_factors(number):
    factors = []
    
    # Iterate from 1 to the given number
    for i in range(1, number + 1):
        # Check if i is a factor of the given number
        if number % i == 0:
            factors.append(i)
    
    return factors

# Get user input for the natural number
try:
    user_input = int(input("Enter a natural number: "))
    
    if user_input > 0:
        result = find_factors(user_input)
        print(f"The factors of {user_input} are: {result}")
    else:
        print("Please enter a positive natural number.")
except ValueError:
    print("Invalid input. Please enter a valid natural number.")

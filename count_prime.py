def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(limit):
    count = 0
    for num in range(2, limit):
        if is_prime(num):
            count += 1
    return count

# Get user input for the limit
try:
    limit = int(input("Enter a non-negative number: "))
    if limit < 0:
        raise ValueError("Please enter a non-negative number.")
    
    # Count primes and display the result
    prime_count = count_primes(limit)
    print(f'There are {prime_count} prime numbers less than {limit}.')
except ValueError as e:
    print(f"Error: {e}")

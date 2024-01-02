from itertools import permutations

def count_combinations(n, s):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    digit_combinations = permutations(digits, n)

    count = 0
    for combination in digit_combinations:
        if sum(combination) == s and len(set(combination)) == n:
            count += 1

    return count

def main():
    try:
        n = int(input("Enter the number of digits (n): "))
        s = int(input("Enter the target sum (s): "))

        if n <= 0 or s < 0 or n > 10:
            raise ValueError("Invalid input. n should be a positive integer between 1 and 10, and s should be a non-negative integer.")

        result = count_combinations(n, s)
        print(f"Number of combinations where the sum is {s}: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

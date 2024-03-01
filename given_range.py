def is_in_range(number, start, end):
    """
    Check if the given number falls within the specified range [start, end].

    Parameters:
    - number: The number to be checked.
    - start: The start of the range (inclusive).
    - end: The end of the range (inclusive).

    Returns:
    - True if the number is within the range, False otherwise.
    """
    return start <= number <= end

# Example usage:
number_to_check = 7
start_range = 5
end_range = 10

if is_in_range(number_to_check, start_range, end_range):
    print(f"{number_to_check} is within the range [{start_range}, {end_range}]")
else:
    print(f"{number_to_check} is outside the range [{start_range}, {end_range}]")

class RomanToInteger:
    def __init__(self):
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_integer(self, s: str) -> int:
        result = 0
        prev_value = 0
        for char in reversed(s):
            value = self.roman_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

# Example usage:
converter = RomanToInteger()
print(converter.roman_to_integer("III"))  # Output: 3
print(converter.roman_to_integer("IV"))   # Output: 4
print(converter.roman_to_integer("IX"))   # Output: 9
print(converter.roman_to_integer("LVIII"))# Output: 58
print(converter.roman_to_integer("MCMXCIV")) # Output: 1994

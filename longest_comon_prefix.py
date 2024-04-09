def longest_common_prefix(strings):
    if not strings:
        return ""

    # Find the shortest string in the list
    shortest = min(strings, key=len)

    for i, char in enumerate(shortest):
        if any(s[i] != char for s in strings):
            return shortest[:i]
    
    return shortest

# Example usage:
strings = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(strings))

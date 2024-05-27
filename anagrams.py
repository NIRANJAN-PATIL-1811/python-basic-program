def group_anagrams(words):
    anagrams = {}
    for word in words:
        # Sort the word to create a key
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    
    # Convert the dictionary values to a list of lists
    return list(anagrams.values())

# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_anagrams = group_anagrams(words)
print(grouped_anagrams)

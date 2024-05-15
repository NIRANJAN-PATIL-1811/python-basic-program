# Define a list of words
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "mango", "nectarine", "orange"]

# Define a function that checks if a word has more than five letters
def has_more_than_five_letters(word):
    return len(word) > 5

# Use the filter function to extract words with more than five letters
long_words = list(filter(has_more_than_five_letters, words))

# Print the resulting list
print(long_words)

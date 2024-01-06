def reverse_words_of_odd_length(sentence):
    words = sentence.split()
    reversed_words = []

    for word in words:
        if len(word) % 2 == 1:  # Check if the length of the word is odd
            reversed_word = word[::-1]  # Reverse the word
            reversed_words.append(reversed_word)
        else:
            reversed_words.append(word)

    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Example usage:
input_sentence = "This is a sample sentence for testing"
result = reverse_words_of_odd_length(input_sentence)
print("Original sentence:", input_sentence)
print("Reversed words of odd lengths:", result)

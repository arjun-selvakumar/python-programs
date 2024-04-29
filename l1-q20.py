def count_words(sentence):
    words = sentence.split()
    return len(words)

# Example usage:
input_sentence = input("Enter a sentence: ")
word_count = count_words(input_sentence)
print(f"Number of words: {word_count}")

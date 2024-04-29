def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Example usage:
input_string = input("Enter a sentence: ")
word_occurrences = count_word_occurrences(input_string)
print("Word Occurrences:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")

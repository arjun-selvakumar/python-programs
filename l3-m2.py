# Get the input text from the user
text = input("Enter the text: ")

# Split the text into words
words = text.split()

# Initialize an empty dictionary to store word frequencies
word_freq = {}

# Count the frequency of each word
for word in words:
    # Remove punctuation marks from the word
    word = word.strip('.,?!')
    # Convert the word to lowercase to ensure case-insensitive counting
    word = word.lower()
    # Update the frequency count for the word
    word_freq[word] = word_freq.get(word, 0) + 1

# Print the dictionary of word frequencies
print("Word frequency count:")
print(word_freq)

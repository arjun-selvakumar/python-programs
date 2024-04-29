# Sample set of valid words
valid_words = {'apple', 'banana', 'orange', 'grape'}

# Get the input document from the user
document = input("Enter the document: ")

# Split the document into words
words = document.split()

# Initialize an empty list to store misspelled words
misspelled_words = []

# Check each word in the document
for word in words:
    # Check if the word is not in the set of valid words
    if word.lower() not in valid_words:
        misspelled_words.append(word)

# Print the misspelled words
print("Misspelled words:", misspelled_words)

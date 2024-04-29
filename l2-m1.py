# Sample list of words
words = ["hello", "world", "python", "programming", "example"]

# Iterate over each word in the list
for word in words:
    # Initialize vowel count for the current word
    vowel_count = 0
    
    # Iterate over each character in the word
    for char in word:
        # Check if the character is a vowel (a, e, i, o, u)
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            # Increment the vowel count if the character is a vowel
            vowel_count += 1
    
    # Print the word along with its vowel count
    print(f"Word: {word}, Vowel Count: {vowel_count}")

# Sample dictionary of translations
translations = {'hello': 'bonjour', 'world': 'monde'}

# Sample English sentence
sentence = input("Enter the English sentence: ")

# Translate the sentence using the dictionary
translated_sentence = ' '.join(translations.get(word, word) for word in sentence.split())

# Print the translated sentence
print("Translated sentence:", translated_sentence)

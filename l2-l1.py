# Sample list of tuples representing (name, age) pairs of people
people = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Initialize an empty dictionary to store the converted data
people_dict = {}

# Iterate over each tuple in the list
for name, age in people:
    # Add each (name, age) pair to the dictionary
    people_dict[name] = age

# Print the resulting dictionary
print("Dictionary with names as keys and ages as values:", people_dict)

# Sample dictionary of lists
dict_of_lists = {'Name': ['John', 'Alice', 'Bob'],
                 'Age': [25, 30, 35],
                 'City': ['New York', 'Paris', 'London']}

# Get the length of the lists (assuming all lists have the same length)
list_length = len(next(iter(dict_of_lists.values())))

# Initialize an empty list to store dictionaries
list_of_dicts = []

# Iterate over the range of list length
for i in range(list_length):
    # Create a new dictionary for each index
    new_dict = {}
    # Populate the new dictionary with values from the original dictionary
    for key, values in dict_of_lists.items():
        new_dict[key] = values[i]
    # Append the new dictionary to the list
    list_of_dicts.append(new_dict)

# Print the list of dictionaries
for dictionary in list_of_dicts:
    print(dictionary)

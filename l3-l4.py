# Sample dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}

# Combine dictionaries by adding values for common keys
combined_dict = {}

# Iterate over keys in dict1
for key in dict1:
    # If key is present in dict2, add the values together
    if key in dict2:
        combined_dict[key] = dict1[key] + dict2[key]
    # Otherwise, add the value from dict1 to the combined dictionary
    else:
        combined_dict[key] = dict1[key]

# Iterate over keys in dict2 to add remaining keys
for key in dict2:
    # If key is not present in combined_dict, add the value from dict2
    if key not in combined_dict:
        combined_dict[key] = dict2[key]

print("Combined dictionary:", combined_dict)

# Sample dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 15, 'e': 25}

# Get the unique values and sort them in descending order
unique_values = sorted(set(data.values()), reverse=True)

# If there are at least two unique values, the second largest exists
if len(unique_values) >= 2:
    second_largest = unique_values[1]
    # Find the corresponding key(s) for the second largest value
    keys = [key for key, value in data.items() if value == second_largest]
    print(f"The second largest value in the dictionary is {second_largest}.")
    print(f"It appears with key(s): {keys}")
else:
    print("There is no second largest value in the dictionary.")

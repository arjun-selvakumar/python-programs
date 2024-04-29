# Sample list of dictionaries
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# Extract values from the dictionaries
values = [value for item in data for value in item.values()]

# Convert the list of values to a set to get distinct values
unique_values = set(values)

# Print the unique values
print("Unique Values:", unique_values)

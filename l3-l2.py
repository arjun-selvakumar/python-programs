# Sample dictionary
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']}

# Find the maximum length of each key for formatting
max_lengths = {key: max(len(str(key)), max(len(str(x)) for x in values)) for key, values in data.items()}

# Print table headers
print("|", end="")
for key, max_length in max_lengths.items():
    print(f" {key.ljust(max_length)} |", end="")
print()

# Print separator
print("+", end="")
for _, max_length in max_lengths.items():
    print(f"-{'-' * max_length}-+", end="")
print()

# Print table rows
for i in range(len(data['Name'])):
    print("|", end="")
    for key, values in data.items():
        print(f" {str(values[i]).ljust(max_lengths[key])} |", end="")
    print()

# Print separator
print("+", end="")
for _, max_length in max_lengths.items():
    print(f"-{'-' * max_length}-+", end="")
print()

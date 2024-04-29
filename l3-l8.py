# Sample dictionary
data = {'a': 2, 'b': 3, 'c': 4}

# Initialize the product variable to 1
product = 1

# Multiply all values together
for value in data.values():
    product *= value

# Print the product
print("Product of all values in the dictionary:", product)

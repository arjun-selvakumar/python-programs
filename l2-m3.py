# Sample lists of integers
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Initialize an empty list to store common elements
common_elements = []

# Iterate over each element in list1
for element in list1:
    # Check if the element is also present in list2
    if element in list2:
        # If the element is common to both lists, append it to common_elements
        common_elements.append(element)

# Print the list containing common elements
print("Common elements:", common_elements)

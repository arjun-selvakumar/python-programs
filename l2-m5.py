# Sample list of names of students in a class
student_names = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]

# Create a new list to store unique names
unique_names = []

# Iterate over each name in the original list
for name in student_names:
    # Check if the name is not already in the unique_names list
    if name not in unique_names:
        # If the name is not a duplicate, add it to the unique_names list
        unique_names.append(name)

# Print the updated list of unique names
print("Updated list of unique names:", unique_names)

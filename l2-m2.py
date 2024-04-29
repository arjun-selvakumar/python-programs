# Sample list of tuples representing names and ages
people = [("Alice", 25), ("Bob", 30), ("Charlie", 40), ("David", 35)]

# Initialize variables to store total age and count of people
total_age = 0
count = 0

# Iterate over each tuple in the list
for person in people:
    # Extract the age from the tuple
    age = person[1]
    
    # Add the age to the total age
    total_age += age
    
    # Increment the count of people
    count += 1

# Calculate the average age
average_age = total_age / count

# Print the average age
print("Average age:", average_age)

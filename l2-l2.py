# Sample list of tuples containing (name, Math score, Physics score, Chemistry score)
students_scores = [("Alice", 90, 85, 95), ("Bob", 80, 75, 85), ("Charlie", 95, 90, 100)]

# Sort the list of tuples based on the total score in descending order
sorted_students = sorted(students_scores, key=lambda x: sum(x[1:]), reverse=True)

# Print the sorted list of tuples
print("Sorted list of tuples based on total score (in descending order):")
for student in sorted_students:
    print(student)

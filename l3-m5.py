# Initialize an empty dictionary to store student grades
grades = {}

# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Get the grades for each student from the user
for i in range(num_students):
    student_name = input(f"Enter the name of student {i+1}: ")
    student_grades = input(f"Enter the grades for {student_name} (comma-separated): ").split(',')
    student_grades = [int(grade.strip()) for grade in student_grades]  # Convert grades to integers
    grades[student_name] = student_grades

# Calculate the average grade for each student
average_grades = {student: sum(grades) / len(grades) for student, grades in grades.items()}

# Print the average grades
print("Average grades:")
for student, avg_grade in average_grades.items():
    print(f"{student}: {avg_grade:.2f}")

# Get the expenses from the user
expenses = {}

# Get the number of categories from the user
num_categories = int(input("Enter the number of categories: "))

# Get the expenses for each category from the user
for _ in range(num_categories):
    category = input("Enter the category: ")
    amounts = input(f"Enter the expenses for {category} (comma-separated): ").split(',')
    expenses[category] = [int(amount.strip()) for amount in amounts]

# Calculate the total expenses for each category
total_expenses = {category: sum(amounts) for category, amounts in expenses.items()}

# Print the total expenses for each category
print("Total expenses:")
print(total_expenses)

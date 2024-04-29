def find_max_in_list(numbers):
    if not numbers:
        return None
    max_number = max(numbers)
    return max_number

# Example usage:
num_list = [float(x) for x in input("Enter numbers separated by space: ").split()]
max_num = find_max_in_list(num_list)
if max_num is not None:
    print(f"The maximum number is {max_num}")
else:
    print("No numbers provided")

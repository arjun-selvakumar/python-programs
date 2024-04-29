def convert_case(s):
    return s.upper(), s.lower()

# Example usage:
input_string = input("Enter a string: ")
upper_case, lower_case = convert_case(input_string)
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")

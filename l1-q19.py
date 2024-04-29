def extract_substring(s, start, end):
    return s[start:end]

# Example usage:
input_string = input("Enter a string: ")
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))
substring = extract_substring(input_string, start_index, end_index)
print("Extracted substring:", substring)

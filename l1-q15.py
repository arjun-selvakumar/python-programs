def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example usage:
input_string = input("Enter a string: ")
num_vowels = count_vowels(input_string)
print(f"Number of vowels: {num_vowels}")

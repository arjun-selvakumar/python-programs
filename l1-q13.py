def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

# Example usage:
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if are_anagrams(s1, s2):
    print("The strings are anagrams of each other")
else:
    print("The strings are not anagrams")

def find_largest(a, b, c):
    if a == b == c:
        print("All numbers are equal")
    elif a == b > c or a == c > b or b == c > a:
        print("Equal numbers are larger")
    else:
        print(max(a, b, c))

# Example usage:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
find_largest(a, b, c)

def arithmetic_operations(x, y):
    print("Sum:", x + y)
    print("Difference:", x - y)
    print("Product:", x * y)
    if y != 0:
        print("Division:", x / y)

# Example usage:
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
arithmetic_operations(x, y)

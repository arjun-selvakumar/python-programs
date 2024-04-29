def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Example usage:
num = int(input("Enter a number: "))
result = factorial(num)
if result is not None:
    print(f"Factorial of {num} is {result}")
else:
    print("Factorial is not defined for negative numbers")

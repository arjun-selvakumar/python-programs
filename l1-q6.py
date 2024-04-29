def sum_of_digits(number):
    sum_digits = sum(int(digit) for digit in str(abs(number)))
    print(f"Sum of digits of {number} is {sum_digits}")

# Example usage:
num = int(input("Enter a number: "))
sum_of_digits(num)

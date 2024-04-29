def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Example usage:
n = int(input("Enter the number of terms for Fibonacci series: "))
fib_sequence = generate_fibonacci(n)
print("Fibonacci Series:", fib_sequence)

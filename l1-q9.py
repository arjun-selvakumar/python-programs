def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print(f"Simple Interest: {interest}")

# Example usage:
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period (in years): "))
calculate_simple_interest(principal, rate, time)

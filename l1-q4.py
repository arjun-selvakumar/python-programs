def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")

# Example usage:
celsius = float(input("Enter temperature in Celsius: "))
celsius_to_fahrenheit(celsius)

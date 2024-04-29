# Sample list of temperatures measured in Celsius
temperatures_celsius = [0, 10, 20, 30, 40]

# Initialize an empty list to store temperatures in Fahrenheit
temperatures_fahrenheit = []

# Convert each temperature from Celsius to Fahrenheit and append to temperatures_fahrenheit
for celsius in temperatures_celsius:
    fahrenheit = (celsius * 9/5) + 32
    temperatures_fahrenheit.append(fahrenheit)

# Print the resulting list of temperatures in Fahrenheit
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)

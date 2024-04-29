# Sample dictionary of room availability
room_availability = {
    'Standard': {'2024-04-12': 10, '2024-04-13': 5},
    'Deluxe': {'2024-04-12': 5, '2024-04-13': 2}
}

# Get the date from the user
date = input("Enter the date (YYYY-MM-DD): ")

# Check the availability of rooms for the given date
availability = {room_type: availability.get(date, 0) for room_type, availability in room_availability.items()}

# Print the availability of rooms for the given date
print("Room availability for", date + ":", availability)

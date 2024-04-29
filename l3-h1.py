# Initialize an empty dictionary to store preferences
preferences = {}

# Get the number of genres from the user
num_genres = int(input("Enter the number of genres: "))

# Get the preferences for each genre from the user
for _ in range(num_genres):
    genre = input("Enter the genre: ")
    movies = input(f"Enter the movies for {genre} (comma-separated): ").split(',')
    preferences[genre] = [movie.strip() for movie in movies]

# Get the user's movie preferences
user_preferences = input("Enter your movie preferences (comma-separated): ").split(',')

# Initialize an empty list to store movie recommendations
recommendations = []

# Check each genre in preferences
for genre, movies in preferences.items():
    # Check if any movies in the genre are not already in the user preferences
    recommended_movies = [movie for movie in movies if movie not in user_preferences]
    # Add recommended movies to the recommendations list
    recommendations.extend(recommended_movies)

# Print the recommendations
print("Recommendations:", recommendations)

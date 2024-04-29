# Initialize an empty dictionary to store the votes
votes = {}

# Get the number of candidates from the user
num_candidates = int(input("Enter the number of candidates: "))

# Get the votes for each candidate from the user
for i in range(1, num_candidates + 1):
    candidate_name = input(f"Enter the name of candidate {i}: ")
    vote_count = int(input(f"Enter the number of votes for {candidate_name}: "))
    votes[candidate_name] = vote_count

# Print the dictionary of votes
print("Dictionary of votes:", votes)

# Print the output
print("Output:")
for candidate, count in votes.items():
    print(f"{candidate}: {count}")

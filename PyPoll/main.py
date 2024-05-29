import csv
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
election_data =  os.path.join(script_dir,'election_data.csv')


# Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Open the CSV file and read the data
with open(election_data, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Extract candidate name from each row
        candidate_name = row['Candidate']
        
        # Count total votes cast
        total_votes += 1
        
        # Update candidate vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Calculate percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {'votes': votes, 'percentage': percentage}

# Find the winner based on popular vote
winner = max(candidates, key=lambda x: candidates[x]['votes'])

# Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Define the file name
file_name = "election_results.txt"

# Create the full path to the file
file_path = os.path.join(script_dir, file_name)

# Write to the file
with open(file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, data in candidates.items():
        file.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"Analysis has been exported to : {file_path}")
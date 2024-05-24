import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Open the CSV file and read the data
with open('Module3Challenge/python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
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

# Write the analysis to a text file
with open('Module3Challenge/python-challenge/PyPoll/analysis/election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, data in candidates.items():
        output_file.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print("Analysis has been exported to election_results.txt")

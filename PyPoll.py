# Import the datetime class from the datetime module
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# Print the present time.
#print("The time right now is ",now)

# Open the election results and read the file
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable for the analysis output
# Then, using with statement open, write data to the analysis output file
file_to_save = os.path.join("analysis","election_analysis.txt")
#with open(file_to_save,"w") as txt_file:
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# 1. Determine total number of votes 
# 1. Initialize total_votes variable
total_votes = 0

# 2. A complete list of candidates who received votes
# 2. Declare a new list for candidates
candidate_options = []

# 3. Determine the total number of votes each candidate won
# 3. Declare a new dictionary for votes per candidate
candidate_votes = {}

# 5. The winner of the election based on popular vote
# 5. Declare variables for winning count and percentage
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Read the file object with the reader function.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print header row
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        #print(row)
        # 1. Add to the total vote count
        total_votes += 1

        # 2. Get candidates names
        candidate_name = row[2]

        # 2. Append candidates to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # 3. Begin tracking each candidate's votes
            candidate_votes[candidate_name] = 0

        # 3. Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# 6. Save results to text files
with open(file_to_save,"w") as txt_file:
    
    Election_Results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(Election_Results,end="")
    txt_file.write(Election_Results)


    # 1. Print the total votes
    # print(total_votes)

    # 2. Print candidate list
    # print(candidate_options)

    # 3. Print candidate vote dictionary
    # print(candidate_votes)

    # 4. The percentage of votes each condidate won
    # 4. Iterate through the candidate list
    for candidate_name in candidate_votes:
        # 4. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        # 4. Calculate percentage of total votes
        vote_percentage = float(votes)/float(total_votes) * 100

        # 4. Print each candidates name, vote count and percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # 5. Print winning candidate information
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


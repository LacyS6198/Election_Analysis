# Import the datetime class from the datetime module
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# Print the present time.
print("The time right now is ",now)

# Open the election results and read the file
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable for the analysis output
# Then, using with statement open, write data to the analysis output file
file_to_save = os.path.join("analysis","election_analysis.txt")
#with open(file_to_save,"w") as txt_file:
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# Read the file object with the reader function.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    # for row in file_reader:
    #     print(row)
    
    #Read and print header row
    headers = next(file_reader)
    print(headers)
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each condidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

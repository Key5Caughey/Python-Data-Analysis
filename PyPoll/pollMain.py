
#read data from csv file budget_data.csv
import os  #to create path
import csv 
#storing path in variable
input_file = "./Resources/election_data.csv"
#creating name for text file
output_file = "analysis.txt"

# setting up variables
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

#reading file ,skipping header
with open(input_file,"r") as file:
    reader = csv.reader(file)
    header = next(reader)

# looping through rows
    for row in reader:
        total_votes = total_votes +1
        candidate_name = row[2]

# setting up conditionals,getting individual candidates names 
# and candidate votes 
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
    
# inside for loop , outside of if statement
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# creating text file and output variables
with open (output_file, "w") as txt_file:
    election_results = (

        f"\n\nElection Analysis\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n"

    )
# printing to terminal
    print (election_results)

# adding to text file
    txt_file.write(election_results)

# looping through candidates , adding  votes , getting percentage
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

# setting conditionals
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage: .3}% ({votes})\n"

        print (voter_output)

        txt_file.write(voter_output)

    winning_summary = (
       f"---------------------------\n"
       f"Winner: {winning_candidate}\n"
       f"---------------------------\n"
    )
# printing in terminal
    print (winning_summary)

#adding to text file
    txt_file.write(winning_summary)




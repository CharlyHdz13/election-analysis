# The data we need to retrieve

import csv
import os

# Assign a variable to load a file from a path.

file_to_load = os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.

total_votes = 0

# Initialize candidate options list

candidate_options=[]

#Open the election results and read the file

with open(file_to_load) as election_data:

    file_reader=csv.reader(election_data)
    
    # Read the header row.

    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.

    for row in file_reader:

        # Add to the total vote count

        total_votes += 1

        # Print the  candidate name from each row

        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list

            candidate_options.append(candidate_name)
        

# Print the total votes

print(f'The number of total votes is: {total_votes}')

# Print candidate list

print(candidate_options)


# Using the with statement open the file as a text file.

# with open(file_to_save,'w') as txt_file:

#     #Write some data to the file.
#     for row in file_reader:
#         txt_file.write(row+'\n')

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 
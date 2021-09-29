# The data we need to retrieve

import csv
import os

# Create a filename variable to a direct or indirect path to the file.

file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Open the election results and read the file

with open(file_to_load) as election_data:

    # To do: Perform analysis

    file_reader=csv.reader(election_data)
    
    #Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    #Print header row
    headers = next(file_reader)
    print(headers)


# Using the with statement open the file as a text file.

with open(file_to_save,'w') as txt_file:

    #Write some data to the file.
    for row in file_reader:
        txt_file.write(row+'\n')

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 
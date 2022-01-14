

import os
import csv

#Read csv file
csvpath = os.path.join('.', 'election_data.csv')

# define Variables as empty lists
total_votes = 0 
candidate_list = []
candidate_dict = {}
winning_vote = 0 
winner = ""

#Opening csv file
with open(csvpath, newline="") as csvfile:
       #read header row
        csvreader = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            # start counting total votes    
            total_votes += 1 
        
            # get the reference to the candidate name from the row 
            candidate = row[2]

            # begin the if statement 
            if candidate not in candidate_list:
            # add the candidate to the list_candidate 
                candidate_list.append(candidate)
                candidate_dict[candidate] = 0

            
            candidate_dict[candidate] +=1 

output_file = 'election_results.txt'
with open(output_file, "w", newline="") as datafile:
    
    # print the total votes 
    print(f"Election Results")
    print(f"--------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------")

    datafile.write(f"Election Results\n")
    datafile.write(f"--------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write(f"--------------------\n")
    
    # loop through the candidates and calculate their percentage of the votes 
    for candidate in candidate_dict: 
        percentage = round(float(candidate_dict[candidate])/float(total_votes),2)

        print(f"{candidate}: {percentage:.3%} ({candidate_dict[candidate]})\n")
        datafile.write(f"{candidate}: {percentage:.3%} ({candidate_dict[candidate]})\n")

        votes = candidate_dict[candidate]
        if votes > winning_vote:
            winning_vote = votes
            winner = candidate

    # print to terminal       
    print(f"--------------------")
    print(f"Winner: {winner}")
    print(f"--------------------")
    # write an output file    
    f.write(f"--------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"--------------------")


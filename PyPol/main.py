#import packages
import csv
import os
#define paths for input and output files
input_csvpath = os.path.join('Resources', 'election_data.csv')
output_txt = os.path.join('Analysis', 'data_analysis.txt')
#creating lists for values on calculation
vote_id = []
candidate = []
unique_candidate = []
percent = []
#Print Statements
print("\n")
print("Election Results")
print("\n---------------------------\n")

#Opens excel file
with open(input_csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #store header rows into a Headers list
    Headers = next(csvreader)
    #set to 0 for counting
    total_votes = 0
    # creates unique lists
    for row in csvreader:
        total_votes += 1
        
        #Determines candidate uniqueness and adds name to list
        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])
            vote_id.append(1)
        else:
            candidate_index = unique_candidate.index(row[2])
            vote_id[candidate_index] += 1
    print(f'Total Votes: {total_votes}')
    print("---------------------------")
    #prints each candidate name, % of votes, and total votes
    for row in range(len(vote_id)):
        percent.append(vote_id[row] / total_votes)
        percentage = round(100*(percent[row]))
        print(f'{unique_candidate[row]}: {percentage:.3f}% ({vote_id[row]})')
    print(f'---------------------------------------')
    print(f'Winner: {unique_candidate[0]}!!!')

#Prints output of the above code
with open(output_txt, 'w') as output:
    output.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {total_votes}\n"
                   f"----------------------------\n"
                   )
    for i in range(len(unique_candidate)):
        output.write(f"{unique_candidate[i]}: {percentage:.3f} ({vote_id[i]})\n")

    output.write(f"----------------------------\n"
                   f"Winner: {unique_candidate[0]}\n"
                   f"----------------------------\n"
                  )    
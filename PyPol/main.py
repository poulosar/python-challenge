import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

vote_id = []
candidate = []
county = []
unique_candidate = []
percent = []

print("\n")
print("Election Results")
print("\n---------------------------\n")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
  # --- store header rows into a Headers list ---
    Headers = next(csvreader)
    total_votes = 0
    # creates unique lists
    for row in csvreader:
        total_votes += 1
        
        #if statement to add candidate name to unique list if not there
        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])
            vote_id.append(1)
        else:
            candidate_index = unique_candidate.index(row[2])
            vote_id[candidate_index] += 1
    print(f'Total Votes: {total_votes}')
    print("---------------------------")
    
    for row in range(len(vote_id)):
        percent.append(vote_id[row] / total_votes)
        percentage = round(100*(percent[row]))
        print(f'{unique_candidate[row]}: {percentage:.3f}% ({vote_id[row]})')
    print(f'---------------------------------------')
    print(f'Winner: {unique_candidate[0]}!!!')





# Print Statements


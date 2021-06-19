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

# Opens csv data to import
with open(input_csvpath) as csvfile:
    # Opens text file for export
    with open(output_txt, 'w') as output:
        # Print statements will appear to duplicate, 
        # output.read will send values to .txt, print to terminal
        output.write("\n")
        print("\n")
        output.write("\nElection Results\n")
        print("Election Results")
        output.write("\n---------------------------\n")
        print("\n---------------------------\n")
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
        output.write(f'\nTotal Votes: {total_votes}\n')
        print(f'Total Votes: {total_votes}')
        output.write("\n---------------------------\n")
        print("---------------------------")
        
        #prints each candidate name, % of votes, and total votes
        for row in range(len(vote_id)):
            percent.append(vote_id[row] / total_votes)
            percentage = round(100*(percent[row]))
            output.write(f'\n{unique_candidate[row]}: {percentage:.3f}% ({vote_id[row]})\n')
            print(f'{unique_candidate[row]}: {percentage:.3f}% ({vote_id[row]})\n')
        output.write(f'\n---------------------------------------\n')
        print(f'---------------------------------------')
        output.write(f'\nWinner: {unique_candidate[0]}!!!\n')
        print(f'Winner: {unique_candidate[0]}!!!')

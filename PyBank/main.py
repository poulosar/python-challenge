import os
import csv
#Creates reference for file paths
input = os.path.join('Resources', 'budget_data.csv')
output_txt = os.path.join('Analysis', 'data_analysis.txt')

#creates lists and variables
months = []
total_change = []
change_over_time = []
count = 0
last_revenue = 0
current_revenue = 0
difference_list = []
full_list = []

with open(input) as csvfile:
    # set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')

    #store header rows into a Headers list
    Headers = next(csvreader)
    
    num_rows = 0
    # Counts each row until none left and then prints output of counter as total months
    for row in csvreader:
        num_rows += 1
        total_change.append(int(row[1]))
    months.append(num_rows)

with open(input) as csvfile:
    # set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip headers
    next(csvreader, None)

    # Counter to find row we're on for adding and average
    if count != int(int(num_rows) - 1):
        for row in csvreader:
            change_over_time.append(int(row[1]))
            full_list.append(row[0])
            last_revenue = change_over_time[count-1]
            current_revenue = change_over_time[count]
            difference_list.append(current_revenue-last_revenue)
            count = count + 1
    # Sets max_value equal to max profit and min_value to min profit
    max_value = max(difference_list)
    min_value = min(difference_list)
    # Gets max value and converts to index, this will be used to pull date of this profit
    max_value_index = difference_list.index(max_value)
    min_value_index = difference_list.index(min_value)
    # This will remove the first entry, this will be 0 and skews results without it, needs to happen after indexing too
    difference_list.pop(0)
    # Prints in console to confirm it runs
    print('\nFinancial Analysis\n')
    print('--------------------------------\n')
    print(f'Total Months: {int(num_rows)}\n')
    print(f'Total: ${int(sum(total_change))}\n')
    print(f'Average Change: ${round(sum(difference_list)/len(difference_list), 2)}\n')
    print(f'Greatest increase in profits: {full_list[int(max_value_index)]}  (${max_value})\n')
    print(f'Greatest decrease in profits: {full_list[int(min_value_index)]}  (${min_value})\n')
#prints to text file reference
with open(output_txt, 'w') as output:
    output.write('\nFinancial Analysis\n')
    output.write('\n--------------------------------\n')
    output.write(f'\nTotal Months: {int(num_rows)}\n')
    output.write(f'\nTotal: ${int(sum(total_change))}\n')
    output.write(f'\nAverage Change: ${round(sum(difference_list)/len(difference_list), 2)}\n')
    output.write(f'\nGreatest increase in profits: {full_list[int(max_value_index)]}  (${max_value})\n')
    output.write(f'\nGreatest decrease in profits: {full_list[int(min_value_index)]}  (${min_value})\n')
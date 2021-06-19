import os
import csv
from typing import Counter

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
total_change = []

with open(csvpath) as csvfile:
    # set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip headers
    next(csvreader, None)

    num_rows = 0
    # Counts each row until none left and then prints output of counter as total months
    for row in csvreader:
        num_rows += 1
    months.append(num_rows)

# Uses budget_data.csv to add all month totals and print it out
with open(csvpath) as csvfile:
    # set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip headers
    next(csvreader, None)
    # Appends net_change with "Profit/Loses" column data
    for row in csvreader:
        total_change.append(int(row[1]))
    # Returns a value of the sum of all values in "Profit/Loses"

# Uses budget_data.csv to get average of changes over time
change_over_time = []
with open(csvpath) as csvfile:
    # set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip headers
    next(csvreader, None)
    # variables for counting, last total profit/loss, and current profit/loss
    count = 0
    last_revenue = 0
    current_revenue = 0
    # List to keep track of each difference to add and average later
    difference_list = []
    full_list = []
    # Counter to find row we're on for adding and average
    if count != int(int(num_rows) - 1):
        for row in csvreader:
            change_over_time.append(int(row[1]))
            full_list.append(row[0])
            last_revenue = change_over_time[count-1]
            current_revenue = change_over_time[count]
            difference_list.append(current_revenue-last_revenue)
            count = count + 1
    #sets max_value equal to max profit from the difference list
    #gets max value and converts to index, this will be used to pull date of this profit
    max_value = max(difference_list)
    min_value = min(difference_list)
    max_value_index = difference_list.index(max_value)
    min_value_index = difference_list.index(min_value)
    # This will remove the first entry, this will be 0 and skews results without it, needs to happen after indexing too
    difference_list.pop(0)
    # Prints the average change from function defined above
    print(f'Total Months: {int(num_rows)}')
    print(f'Total: ${int(sum(total_change))}')
    print(f'Average Change: ${round(sum(difference_list)/len(difference_list), 2)}')
    print(f'Greatest increase in profits: {full_list[int(max_value_index)]}  (${max_value})')
    print(f'Greatest increase in profits: {full_list[int(min_value_index)]}  (${min_value})')
  
import os
import csv
from typing import Counter

csvpath = os.path.join('Resources', 'budget_data.csv')

#Function that uses budget_data.csv to get total number of months in csv, this should work on any number of entries
def total_months():
    months = []
    with open(csvpath) as csvfile:
    #set delimiter as ,
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip headers
        next(csvreader, None)

        num_rows = 0
        #Counts each row until none left and then prints output of counter as total months
        for row in csvreader:
            num_rows += 1
        months.append(num_rows)
        return(int(num_rows))
#Prints the above function with the string "Total Months"
print("Total Months: " + str(total_months()))

#Uses budget_data.csv to add all month totals and print it out
def total_net_change():
    net_change = []
    with open(csvpath) as csvfile:
        #set delimiter as ,
        csvreader = csv.reader(csvfile, delimiter=',')
    
        #skip headers
        next(csvreader, None)
        #Appends net_change with "Profit/Loses" column data
        for row in csvreader:
            net_change.append(int(row[1]))
        #Returns a value of the sum of all values in "Profit/Loses"
        return(int(sum(net_change)))
#This runs the definition above to print out results
print(f'Total: ${int(total_net_change())} ')
#
#
#Uses budget_data.csv to get average of changes over time
change_over_time = []
with open(csvpath) as csvfile:
    #set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip headers
    next(csvreader, None)
    #Start at the second entry to get difference and avoid errors
    count = 0
    last_value = 0
    current_value = 0
    #List to keep track of each difference to add and average later
    difference = []
     #Counter to find row were on for adding and average
    if count != int(total_months()- 1):
        for row in csvreader:
            change_over_time.append(int(row[1]))
            last_value = change_over_time[count-1]
            current_value = change_over_time[count]
            difference.append(current_value-last_value)
            # print(difference)
            # print("------------------------------------------------------")
            # print(change_over_time)
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            count = count + 1
    difference.pop(0)
    print(round(sum(difference)/len(difference),2))
    # print(change_over_time[count-1])
   

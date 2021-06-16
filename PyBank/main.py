import os
import csv
from typing import Counter

csvpath = os.path.join('Resources', 'budget_data.csv')

#Function that uses budget_data.csv to get total number of months in csv, this should work on any number of entries
def total_months():
    with open(csvpath) as csvfile:
    #set delimiter as ,
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip headers
        next(csvreader, None)

        num_rows = 0
        #Counts each row until none left and then prints output of counter as total months
        for row in csvreader:
            num_rows += 1
        return(str(num_rows))
#Prints the above function with the string "Total Months"
print("Total Months: " + str(total_months()))

#Uses budget_data.csv to add all month totals and print it out
Total = []
with open(csvpath) as csvfile:
    #set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip headers
    next(csvreader, None)
    #Adds each row, column 2 to the list total and then prints the sum of each row
    for row in csvreader:
        Total.append(int(row[1]))
    print("Total: " + "$" + str(sum(Total)))

#Uses budget_data.csv to find an average of changes over time
average = []
with open(csvpath) as csvfile:
    #set delimiter as ,
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip headers
    next(csvreader, None)
    #Adds each row, column 2 to the list total and then prints the sum of each row
    for row in csvreader:
        Total.append(int(row[1]))
    
    print("Total: " + "$" + str(sum(Total)))
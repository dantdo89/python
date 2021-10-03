import os
import csv

csvpath = os.path.join("/Users/dantdo/Desktop/GitHub/python-challenge/PyBank/Resources/budget_data.csv")

total_month = []
total_profit = []
profit_change = []
monthly_change = []
previous_value = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_reader = next(csvreader)

    for row in csvreader:

        total_month.append(row[0])
        #total_profit.append(row[1])

        print("Total months: " + str(len(total_month)))

        #total_profit=[int(x) for x in total_profit] 
        #total_profit_sum=sum(total_profit) 
        #print (total_profit_sum) 

#for i in range(len(total_profit)-1):
    #monthly_change.append(total_profits[i+1]-total_profit[i])
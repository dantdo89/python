import os
import csv 

csvpath = os.path.join('/Users/dantdo/Desktop/GitHub/python-challenge/PyBank/Resources/budget_data.csv')
totalmonth = 0
totalprofitloss = 0
previousprofitloss = 0
profitlosschange = 0
profitlosschangelist = []
monthchange = []
greatestincrease = 0
greatestdecrease = 1000

with open(csvpath) as profitlossdata:
   reader = csv.DictReader(profitlossdata)
   index=0
   for row in reader:
       if(index==0):
           totalmonth+=1
           totalprofitloss = totalprofitloss + int(row["Profit/Losses"])
           previousprofitloss = int(row["Profit/Losses"])
           monthchange = monthchange + [row["Date"]]
           index+=1
           continue

       totalmonth = totalmonth + 1
       totalprofitloss = totalprofitloss + int(row["Profit/Losses"])
       profitlosschange = int(row["Profit/Losses"]) - previousprofitloss
       profitlosschangelist.append(profitlosschange)
       previousprofitloss = int(row["Profit/Losses"])
       monthchange = monthchange + [row["Date"]]
      
   greatestdecrease=min(profitlosschangelist)
   greatestincrease=max(profitlosschangelist)
   
   greatestdecreasemonth=profitlosschangelist.index(greatestdecrease)+1
   greatestincreasemonth=profitlosschangelist.index(greatestincrease)+1

   print("*")
   
   print("Financial Analysis")

   print("*")

   print(f"Total Months: {totalmonth}\n")
   
   print(f"Total Profit/Losess: ${totalprofitloss}\n")
   print(f"Average Change: ${round(sum(profitlosschangelist)/len(profitlosschangelist),2)}")

   print(f"Greatest increase in Profits: {monthchange[ greatestincreasemonth]} (${(str(greatestincrease))})")

   print(f"Greatest decrease in Profits: {monthchange[greatestdecreasemonth]} (${(str(greatestdecrease))})")
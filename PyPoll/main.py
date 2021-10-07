import os
import csv

csvpath = os.path.join('/Users/dantdo/Desktop/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    

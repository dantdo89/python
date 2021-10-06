import os
import csv
import pandas as pd

csvpath = os.path.join('/Users/dantdo/Desktop/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
election_df = pd.read_csv(csvpath)

total_votes = election_df.shape[0]

candidate_group_by_count = election_df.groupby(['Candidate']).count()['Voter ID']

candidate_list = list(candidate_group_by_count.index)

candidate_vote_count_list = list(candidate_group_by_count.values)

candidate_vote_percent_list = []
for candidate_vote_count in candidate_vote_count_list:

  vote_percent = (candidate_vote_count * 100) / total_votes

  vote_percent = round(vote_percent, 3)

  candidate_vote_percent_list.append(vote_percent)

index = candidate_vote_count_list.index(max(candidate_vote_count_list))
winner = candidate_list[index]

election_result = 'Election Result:\n'
election_result += '-'*20
election_result += f'\nTotal Votes: {total_votes}\n'
election_result += '-'*20

for candidate_name, vote_percent, vote_count in zip(candidate_list, candidate_vote_percent_list, candidate_vote_count_list):
  election_result += f'\n{candidate_name}: {vote_percent}% ({vote_count})'

election_result += '\n'
election_result += '-'*20
election_result += f'\nWinner: {winner}\n'
election_result += '-'*20

print(election_result)

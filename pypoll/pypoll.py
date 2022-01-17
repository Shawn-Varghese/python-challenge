import csv 
import os

cwd = os.getcwd()
csv_path = os.path.join(cwd, 'election_data.csv')
#print(csv_path)

canidate_list = []
total_votes = 0
percentage_list = []
percent = 0
total_num_votes = []
elec_winner = str()
candidates = []



with open(csv_path ,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for i in csvreader:
        total_votes += 1 

        if i[2] not in candidates:
            candidates.append(i[2])
            canidate_list = candidates.index(i[2])

            total_num_votes.append(1)
        else:
            canidate_list = candidates.index(i[2])

            total_num_votes[canidate_list] += 1
    
    for i in total_num_votes:
        percent = ( i / total_votes) * 100
        percentage_list.append(percent)

    #print(percentage_list)

    popular_elec_w = max(total_num_votes)
    canidate_list = total_num_votes.index(popular_elec_w)
    popular_vote = candidates[canidate_list]


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for i in range(4):
    print(f"{candidates[i]}: {str(percentage_list[i])} ({str(total_num_votes[i])})")
print("-------------------------")
print("Winner: " + str(popular_vote))
print("-------------------------")

pypoll_export = open("pypoll_results.txt" , "w")
line_1 = "Election Results"
line_2 = "-------------------------"
line_3 = "Total Votes: " + str(total_votes)
line_4 = "-------------------------"
pypoll_export.write('{}\n{}\n{}\n{}\n'.format(line_1 ,line_2, line_3, line_4))

for i in range(4):
    line_x = str(f"{candidates[i]}: {str(percentage_list[i])} ({str(total_num_votes[i])})")

    pypoll_export.write('{}\n'.format(line_x))
line_5 = "-------------------------"
line_6 = "Winner: " + str(popular_vote)
line_7 = "-------------------------"

pypoll_export.write('{}\n{}\n{}\n'.format(line_5 , line_6, line_7))


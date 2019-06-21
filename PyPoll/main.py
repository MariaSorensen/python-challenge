# Import the os module to allow us to create file
# paths across operating systems and Module 
# for reading CSV files
import os
import csv
from collections import Counter

# Path to collect data from the csv file in the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# open the csv file
with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable 
    # that hold its contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print title to the screen
    print(f"Election Results")
    print(f"--------------------")
    
    # Read the header row first (skip this step if there 
    # is no header)
    csv_header = next(csvreader)
    
    # Calulate the total number of votes cast and print it 
    # to the screen
    value = len(list(csvreader))
    
    print(f"Total number of votes cast: " + str(value))
    print(f"--------------------")

 
# Calulate the total number of votes
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

from pprint import pprint
# Path to collect data from the csv file in the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')
#open the csv file
with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')  
    csv_header = next(csvreader)
    #print(csv_header)

    #Calulates the total number of votes
    #totalC = len(list(csvreader))
    #print(totalC)
    #A complete list of candidates who received votes
    result = {}
    candTotal = 0
    avg = 0
    for cand in csvreader:
        candTotal += 1
        #print(cand)
        if cand[2] not in result:
            result[cand[2]] = 1
            #print(result) 
        else:     
            result[cand[2]] = result[cand[2]] + 1

    
    output_file = os.path.join("output", "PollReport.txt")
    with open(output_file, "w", newline="") as pollrep:       
        for k, v in result.items():
        
            avg = '{0:.4%}'.format(v/candTotal)
            #Print to screen
            print(k, avg, '(',v,')')
            polldata = f'{k} {avg} "("{v},")"' 

            #Print to file
            pollrep.writelines(polldata)
        winner = max(result.values()) 
        winnername = max(result, key=result.get)   
        print('--------------------')
        print(f'Winner: {winnername} {winner}')
        print('--------------------')
        
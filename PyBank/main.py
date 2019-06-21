# Import the os module to allow us to create file
# paths across operating systems and Module 
# for reading CSV files
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(f"csv file: {csvreader}")
    
    # Read the header row first (skip this step if there is no header)
    # Then print the headers
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Get total number of months included in the dataset and print
    value = len(list(csvreader))
    print("Total Months: " + str(value))
    


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    CalcValues = [ ]
    #DValues = [ ]
    #-----------------------------------------------------------------------
    #Go through each row of the file to get the greatest increase in profits
    # (date and amount) over the entire period
    maxChange = 0
    minChange = 0
    PLchange = 0
    PLtotal = 0
    NumberOfLines = 0
    #Loop to get the greatest (max) value date and amount
    for i, row in enumerate(csvreader):
        PLtotal += int(row[1])
        if i > 0:
            change = int(row[1]) - prevPL
            NumberOfLines += 1
            PLchange += change
            #print(f'value change {PLtotal}')

            if change > maxChange:
                maxChange = change
                #print(f'MaxC = {maxChange}')
                dateofMax = row[0]
            elif change < maxChange: 
                if change < minChange:
                    minChange = change
                    #print(f'MinC = {minChange}')
                    dateofMin = row[0]
            else:
                print("I'm not sure")
        
          
        prevPL = int(row[1])
        
    print(f'The total net amount of P/L over the entire period: {PLtotal}')
    average = float(PLchange)/ float(NumberOfLines)
    average = format(average, '.2f')
    print(f'The average CHANGE in Profit/Losses: {average}')
    print(f'Greatest Increase in Profits: {dateofMax} ({maxChange})')
    print(f'Greatest Decrease in Profits:  {dateofMin} ({minChange})')
    #------------------------------------------------------------------------
    # Specify the file to write to
    
    newdata = (f'The total net amount of P/L: {PLtotal}, The average CHANGE in Profit/Losses: {average},  Greatest Increase in Profits: {dateofMax}, {maxChange}, Greatest Decrease in Profits: {dateofMin}, {minChange}')
    output_file = os.path.join("output", "PLstats.txt")
 
    #  Open the output file
    with open(output_file, "w", newline="") as statsreport:
        #statsreport.write(data + '\n')
        #statsreport.write(data2 + '\n')
        statsreport.writelines(newdata)

        
    #print(data1, data2, file=open(output_path, 'w'))

import os
import csv

#declare variables as empty lists
months = []    
greatestIncrease = 0
p = []
average_net_change = 0
total_months = 0
net_change = []

#read csv file
csvpath = os.path.join('.', 'budget_data.csv')

#Open and read csv file
with open(csvpath, newline="") as csvfile:
    
    #read header and set it aside
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
    next(reader, None)

# Loop and put data into list
    for row in reader:
        month = row[0]
        months.append(month)
        values = int(row[1])
        p.append(values)

#count the number of months      
total_months = len(months)
net_total = sum(p)
net_total_months = len(months) - 1
difference_budget_data = []

for i in range(len(p) - 1):
    difference_budget_data.append(float(p[i + 1]) - float(p[i]))
    new_net_total = sum(difference_budget_data)

 # Find the sum of profits/losses
average_net_change = new_net_total/net_total_months

# Find the greatest increase/decrease (date and amount) over the entire period
min_p = p[p.index(min(p))] - p[p.index(min(p))-1]
max_p = p[p.index(max(p))] - p[p.index(max(p))-1]

# Print out results to console
print("Financials Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_net_change,2)}")
print(f'Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})')
print(f"Greatest Descrease in Profits: {months[p.index(min(p))]} (${min_p})")

#now write in an output file
f = open("financial_analysis.txt", "w")
f.write("Financials Analysis")
f.write("--------------------")
f.write(f"Total Months: {total_months}")
f.write(f"Total: ${net_total}")
f.write(f"Average Change: ${round(average_net_change,2)}")
f.write(f'Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})')
f.write(f"Greatest Descrease in Profits: {months[p.index(min(p))]} (${min_p})")

 

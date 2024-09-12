# using modules from python libraries 
#read data from csv file budget_data.csv
import os  #to create path
import csv 

# storing path to csv data in variable input_file
input_file = "./Resources/budget_data.csv"
#creating name for text file
output_file = "analysis.txt"                      

#initiate variables
total_months = 0            # variable to hold months , counter set to 0, integer
month_of_change = []        # variable to hold monts of change in a list []
net_change_list =[]         # variable to hold net change in a list []
greatest_inc = ["",0]       # variable to hold string and int (greatest increase) in a list []
greatest_dec = ["", 99999999]  # variable to hold string and int (greatest decrease)in a list[]
total_net = 0               # variable to total net , counter set to 0, integer

#reading csv file 
with open (input_file,"r") as file:
    reader = csv.reader(file)
    header = next(reader)
    first_row = next(reader)
    
#adding months
    total_months += 1

    total_net += int(first_row[1])
    prev_net = int(first_row[1])

#for loop to iterate through rows
    for row in reader:
        total_months += 1
        total_net += int (row[1])

# updating variables
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += row[0]

# setting conditiionals,storing results
        if net_change > greatest_inc[1]:
            greatest_inc[1] = net_change
            greatest_inc[0] = row[0]

        if net_change < greatest_dec[1]:
            greatest_dec[1] = net_change
            greatest_dec[0] = row[0]

# calculating net mnthly avg, storing results
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# creating an output tuple in output variable
output = (
    
    f"Financial Analysis\n"
    f"--------------------------------------\n\n" # \n is new line character anything after this 
    f"Total Month: {total_months}\n"              # will appear on the next line,\n,\n skips 2 lines
    f"Total Net: ${total_net} \n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Inc: {greatest_inc[0]} (${greatest_inc[1]})\n"
    f"Greatest Decrease: {greatest_dec[0]} (${greatest_dec[1]})\n\n"
    f"--------------------------------------"
)
#printing the results to terminal using output variable 
print(output)

# storing output in text file analysis.txt output_file was named analysis.txt in begining of program
# open function opens file(analysis.txt) "w"argument means file will opened in write mode

with open(output_file, "w") as txt_file:
    txt_file.write(output) # this writes the info in output variable into txt.file 



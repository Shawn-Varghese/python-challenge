import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

csv_path = os.path.join('budget_data.csv')
#print(csv_path)

total_months = 0 
net_total = 0 
changes = 0
greatest_increase = 0 
greatest_decrease = 0 
last_revenue_value = 0
last_revenue_container = []
min_change = 0
min_date = str()
max_change = 0
max_date = str()

with open(csv_path ,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for i in csvreader:
        total_months += 1 
        net_total += eval(i[1])

        if last_revenue_value != 0:
            revenue_diff = eval(i[1]) - last_revenue_value
            last_revenue_container.append(revenue_diff)

            if revenue_diff > max_change:
                max_date = i[0]
                max_change = revenue_diff

            if revenue_diff < min_change:
                min_date = i[0]
                min_change = revenue_diff

        last_revenue_value = eval(i[1])
        
Ave_of_change = sum(last_revenue_container) / len(last_revenue_container)


print("Financial Analysis")
print("----------------------------")
print("Total Months:", str(total_months))
print("Total: $" + str(net_total))
print("Average  Change: $" + str(Ave_of_change))
print("Greatest Increase in Profits:", max_date, '($'+str(max_change)+')')
print("Greatest Decrease in Profits:", min_date, '($'+str(min_change)+')')


pybank_export = open("pybank_results.txt" , "w")
line_1 = "Financial Analysis"
line_2 = "----------------------------"
line_3 = "Total Months:", str(total_months)
line_4 = "Total: $" + str(net_total)
line_5 = "Average  Change: $" + str(Ave_of_change)
line_6 = "Greatest Increase in Profits:", max_date, '($'+str(max_change)+')'
line_7 = "Greatest Decrease in Profits:", min_date, '($'+str(min_change)+')'

pybank_export.write(
    '{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line_1 ,line_2, line_3, line_4, line_5, line_6, line_7))
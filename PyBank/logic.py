import csv
import os

myfile = os.path.join(os.path.expanduser('~'),"google drive","rice big data bootcamp","hw", "hw3","resources","budget_data.csv")

with open(myfile) as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)

    #   variables  
    number_of_months = 0
    total_amount = 0
    previous_profit = 0
    previous_month = ''
    previous_loss = 0
    previous_month_loss = ''
    greatest_increase_month = ''
    greatest_increase = 0
    greatest_decrease_month = ''
    greatest_decrease = 0

#   functionality
    for row in csv_reader:
        number_of_months += 1
        total_amount = total_amount + int(row[1])
        # greatest increase
        if (int(row[1]) - previous_profit) > greatest_increase:
            greatest_increase = ( int(row[1]) - previous_profit )
            greatest_increase_month = row[0]
        previous_profit = int(row[1])
        # greatest decrease
        if (int(row[1]) - previous_loss) < greatest_decrease:
            greatest_decrease = ( int(row[1]) - previous_loss )
            greatest_decrease_month = row[0]
        previous_loss = int(row[1])
 #  show
    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {number_of_months}')
    print(f'Total: $ {total_amount}')
    print(f'Average  Change: $ ')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

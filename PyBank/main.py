import csv

with open('C:/Users/Administrator/Google Drive/Rice Big Data Bootcamp/hw/hw3/Resources/budget_data.csv') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')

#   variables  
    line_count = 0
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
    change = 0
    sum_change = 0
    number_of_changes = 0
    average_change = 0

#   functionality
    for row in csv_reader:
        if line_count == 0:
             line_count += 1
        else:
            line_count += 1
            number_of_months += 1
            total_amount = total_amount + int(row[1])
            # average
            if line_count > 2:
                change = int(row[1]) - previous_profit
                number_of_changes += 1
                sum_change = sum_change + change
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
    average_change = sum_change / number_of_changes
    average_change = round(average_change,2)
 #  output to screen
    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {number_of_months}')
    print(f'Total: $ {total_amount}')
    print(f'Average  Change: $ {average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
 #  output to file   
    pybankfile = open("hw3pybank.txt", "a")
    pybankfile.write(f'Financial Analysis')
    pybankfile.write(f'----------------------------')
    pybankfile.write(f'Total Months: {number_of_months}')
    pybankfile.write(f'Total: $ {total_amount}')
    pybankfile.write(f'Average Change: $ {average_change}')
    pybankfile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    pybankfile.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
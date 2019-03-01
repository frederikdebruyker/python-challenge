import csv
import os

myfile = os.path.join(os.path.expanduser('~'),"google drive","rice big data bootcamp","hw", "hw3","resources","budget_data.csv")
# relative path not used as github is complaining about the storing of the large file
with open(myfile) as csv_file:    
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
#   CSV NEXT is well understood but I finished this homework before we were taught this functionality
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
    with open('pybank_file.csv', mode='w') as pybank_file:
        pybank_writer = csv.writer(pybank_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        pybank_writer.writerow([f'Financial Analysis'])
        pybank_writer.writerow([f'----------------------------'])
        pybank_writer.writerow([f'Total Months: {number_of_months}'])
        pybank_writer.writerow([f'Total: $ {total_amount}'])
        pybank_writer.writerow([f'Average Change: $ {average_change}'])
        pybank_writer.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})'])
        pybank_writer.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})'])
   

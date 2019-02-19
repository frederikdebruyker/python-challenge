import csv
with open('Resources/budget_data.csv', newline='') as csvfile:
           filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
           for row in spamreader:
                print(', '.join(row))
import csv

#with open('C:/Users/Administrator/Google Drive/Rice Big Data Bootcamp/hw/hw3/Resources/budget_data.csv') as csv_file:    
with open('C:/Users/Administrator/Google Drive/Rice Big Data Bootcamp/hw/hw3/Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} , {row[1]}')
            line_count += 1
        print(f'Processed {line_count} lines.')
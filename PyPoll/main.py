# PyPoll
# Frederik De Bruyker
# Rice Big Data Bootcamp - Feb - Aug 2019

# import libraries
import csv
import os

# import csv file(s)
myfile = os.path.join(os.path.expanduser('~'),"google drive","rice big data bootcamp","hw", "hw3","resources","election_data.csv")
# relative path not used as github is complaining about the storing of the large file
with open(myfile) as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)

#   variables  
    line_count = 0
    total_votes = 0
    candidates_list = []
    candidates_totals = []
    index = 0
    highest = 0
    highest_name = ''

#   functionality
    for row in csv_reader:
        total_votes += 1
        if row[2] in candidates_list:
            # candidate is already in our list
            index = candidates_list.index(row[2])
            candidates_totals[index] += 1
        else:
            # candidate is not yet in our list
            candidates_list.append(row[2])
            candidates_totals.append(1)


  #  output to screen
    print(f'Election Results')
    print(f'----------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'----------------------------')
    line_count = 0
    max = len(candidates_list)
    for max in candidates_list:
        percentage = candidates_totals[line_count] / total_votes * 100
        print(f'{candidates_list[line_count]}: {percentage:.3f}% ({candidates_totals[line_count]})')
        if percentage > highest:
           highest = percentage
           highest_name = candidates_list[line_count]
        line_count += 1
    print(f'----------------------------')
    print(f'Winner: {highest_name}')
    print(f'----------------------------')
  #  output to file   
    with open('pypoll_file.csv', mode='w') as pypoll_file:
        pypoll_writer = csv.writer(pypoll_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        pypoll_writer.writerow([f'Election Results'])
        pypoll_writer.writerow([f'----------------------------'])
        pypoll_writer.writerow([f'Total Votes: {total_votes}'])
        pypoll_writer.writerow([f'----------------------------'])

        line_count = 0
        max = len(candidates_list)
        for max in candidates_list:
            percentage = candidates_totals[line_count] / total_votes * 100
            pypoll_writer.writerow([f'{candidates_list[line_count]}: {percentage:.3f}% ({candidates_totals[line_count]})'])
            if percentage > highest:
                highest = percentage
                highest_name = candidates_list[line_count]
            line_count += 1
        pypoll_writer.writerow([f'----------------------------'])
        pypoll_writer.writerow([f'Winner: {highest_name}'])
        pypoll_writer.writerow([f'----------------------------'])
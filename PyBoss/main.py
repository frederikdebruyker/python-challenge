# PyBoss
# Frederik De Bruyker
# Rice Big Data Bootcamp - Feb - Aug 2019

# import libraries
import csv
import os
import us

myfile = os.path.join(os.path.expanduser('~'),"google drive","rice big data bootcamp","hw", "hw3","resources","employee_data.csv")
# relative path not used as github is complaining about the storing of the large file
with open(myfile) as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')
    # do not consider next(csv_reader, None) in this program

#   variables  
    line_count = 0
    usstatecode = us.states.mapping('name','abbr')
 
#   functionality
    # open the file to write to
    with open('pyboss_file.csv', mode='w') as pyboss_file:
        pyboss_writer = csv.writer(pyboss_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        pyboss_writer.writerow([f'Financial Analysis'])

        # roll through the file
        for row in csv_reader:
            # convert the data
            if line_count == 0:
                # process header
                # write to the file
                pyboss_writer.writerow([f'{row[0]},First Name,Last Name,{row[2]},{row[3]},{row[4]}'])
                print(f'{row[0]},header')
            else:
                # process data
                name = row[1].split()
                # write to the file
                pyboss_writer.writerow([f'{row[0]},{name[0]},{name[1]},{row[2][5:7]}/{row[2][8:]}/{row[2][:4]},***-**{row[3][6:]},{usstatecode[row[4]]}'])
                print(f'{row[0]},{name[0]},{name[1]},{row[2][5:7]}/{row[2][8:]}/{row[2][:4]},***-**{row[3][6:]},{usstatecode[row[4]]}')
            line_count += 1
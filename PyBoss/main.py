import csv
# import us

with open('C:/Users/Administrator/Google Drive/Rice Big Data Bootcamp/hw/hw3/Resources/employee_data.csv') as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')

#   variables  
    line_count = 0
    # compliments of github https://gist.github.com/rogerallen/1583593 - python dictionary object
    usstatecode = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

#   functionality
    # open the file to write to
    pybossfile = open("hw3pyboss.txt", "a")
    pybossfile.write(f'Financial Analysis')

    # roll through the file
    for row in csv_reader:
        # convert the data
        if line_count == 0:
            # process header
            # write to the file
            pybossfile.write(f'{row[0]},First Name,Last Name,{row[2]},{row[3]},{row[4]}')
            print(f'{row[0]},header')
        else:
            # process data
            name = row[1].split()
            # write to the file
            pybossfile.write(f'{row[0]},{name[0]},{name[1]},{row[2][5:7]}/{row[2][8:]}/{row[2][:4]},***-**{row[3][6:]},{usstatecode[row[4]]}')
            print(f'{row[0]},{name[0]},{name[1]},{row[2][5:7]}/{row[2][8:]}/{row[2][:4]},***-**{row[3][6:]},{usstatecode[row[4]]}')
        line_count += 1
        



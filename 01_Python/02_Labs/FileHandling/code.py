import csv

#f1 = open('file.txt', 'r')

#print(f1.read()) # reads entire file

#f1.seek(0)

#print(f1.readlines())

#f1.seek(0)

#print(f1.readlines(57))

#f1.seek(0)

""" 
# reads last n lines
n = 5

last_n_lines = f1.readlines()[:n] 

print(last_n_lines) """

""" 
# remove line spaces
lines = f1.readlines()

for line in lines:
    print(line.strip()) """

#print(f1.readline(59)) # only reads the first line

""" print(f1.readline()) #first line
print(f1.readline()) #second line
print(f1.readline()) #third line

print(type(f1.readline())) """

#file = open('data.csv', 'r+')
#file_lines = file.readlines()

""" for line in file_lines:
    print(line.strip(",")) """

""" for line in file_lines:
    line = line.strip()  # Remove leading/trailing whitespace and newline characters
    columns = line.split(',')  # Split the line into columns using the comma delimiter

    # Process the columns as needed
    for column in columns:
        print(column)  # Print or manipulate the column data """

with open('data.csv', 'r+') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for row in rows:
        print(row)

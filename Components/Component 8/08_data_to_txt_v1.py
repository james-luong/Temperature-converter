# Source: https://www.guru99.com/reading-and-writing-files-in-python.html

# Data to be outputed
import weakref

data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank
# assume valid data for now

filename = input('Enter a filename: ')

# create file to hold data
file = open(filename, 'w+')

for item in data:
    file.write(item)

# close file
file.close()
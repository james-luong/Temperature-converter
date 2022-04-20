# Source: https://www.guru99.com/reading-and-writing-files-in-python.html

# Data to be outputed

data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank
# assume valid data for now

filename = input('Enter a filename (leave off the extension): ')

# add .txt suffix
filename += '.txt'

# create file to hold data
file = open(filename, 'w+')

# add new line at the end of each line
for item in data:
    file.write(item + '\n')

# close file
file.close()
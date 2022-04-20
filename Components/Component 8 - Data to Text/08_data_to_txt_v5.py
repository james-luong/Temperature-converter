# Source: https://www.guru99.com/reading-and-writing-files-in-python.html

# Need to import the RegEx library
import re

# data to be outputed
data = ['I', 'love', 'computer']

# Get filename, can't be blank
# Assume valid data for now

has_error = 'yes'
while has_error == 'yes':
    problem = ''
    has_error = 'no'

    filename = input('Enter a filename (leave off the extension): ')

    # RegEx to check file name, can be upper or lower case letters
    valid_char = '[A-Za-z0-9_]' # numbers or underscores

    for letter in filename:
        if re.match(valid_char, letter):
            continue # if the letter is valid, gets back and checks the next

        elif letter == ' ': # otherwise, find problem
            problem = 'No spaces allowed!'

        else:
            problem = f'No {letter} is allowed!'

        has_error = 'yes'

    if filename == '':
        problem = 'Filename cannot be blank'
        has_error = 'yes'

    if has_error == 'yes': # describe problem
        print(f'Invalid filename - {problem}')

    else:
        print('Filename is valid') # or allow valid file name

# add /txt suffix
filename = filename + '.txt'

# Create file to hold data
f = open(filename, 'w+')

# add new line at the end of each item
for item in data:
    f.write(item + '\n')

# close file
f.close()
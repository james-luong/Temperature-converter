# Source: https://www.guru99.com/reading-and-writing-files-in-python.html
# Includes RegEx to check filename is valid (A-Z, a-z, 0-9 and underscores)
# Check if filename is valid

import re

has_error = 'yes'
while has_error == 'yes':
    problem = ''
    print()

    filename = input('Enter a filename (leave off the extension): ')
    has_error = 'no'

    valid_char = '[A-Za-z0-9_]'

    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == ' ':
            problem = 'No spaces allowed!'

        else:
            problem = f'No {letter} is allowed!'

        has_error = 'yes'

    if filename == '':
        problem = 'Filename cannot be blank'
        has_error = 'yes'

    if has_error == 'yes':
        print(f'Invalid filename - {problem}')

    else:
        print('Filename is valid')
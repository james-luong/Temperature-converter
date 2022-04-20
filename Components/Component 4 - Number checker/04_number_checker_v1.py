# Code to check that a number is valid

def temp_check(low, deg):
    valid = False

    while not valid:
        try:
            response = float(input('Enter a number: '))

            if response < low:
                print(f'Temperature under {low}{deg} cannot be converted')

            else:
                return response

        except ValueError:
            print('Please enter A NUMBER!')


# Main routine
# Set up to run this code twice (for two valid responses in test plan)

number = temp_check(-273, 'C')
print(f'You entered {number}')

number = temp_check(-459, 'F')
print(f'You entered {number}')
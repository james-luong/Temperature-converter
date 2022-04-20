"""Get data from user and store it in a list,
then display the most recent 3 entries
Final version based on trial #3
Adds break loop and checks for empty list"""

# Set up empty list
history_list = []

# Get items of data and add to list
get_item = ''
while get_item != 'zz':
    get_item = input('Enter and item: ')

    if get_item == 'zz':
        break

    history_list.append(get_item)

print()

if len(history_list) == 0:
    print('History list is empty!')

else:

    # Show that everything made it to the list
    print()
    print('*** Full list ***')
    print(history_list)

    # Print items starting at the END of the list
    if len(history_list) >= 3:
        print('*** Most recent 3 ***')
        for item in range(3):
            print(history_list[len(history_list) - item - 1])

    else:
        print('*** Items from Newest to Oldest ***')
        for item in history_list:
            print(history_list[len(history_list) - history_list.index(item) -
                               1])




"""Get data from user and store it in a list,
then display the most recent 3 entries
Trial #1 - uses a list with reverse order"""

# Set up empty list
history_list = []

# Get five items of data
for item in range(5):
    get_item = input('Enter a number: ')
    history_list.append(get_item)

history_list.reverse()

# Show that everything made it to the list
print()
print('Full list')
print(history_list)

print()
print('Most recent 3')
for item in range(3):
    print(history_list[item])


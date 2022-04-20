"""Get data from user and store it in a list,
then display the most recent 3 entries
Trial #3 - prints list in reverse order
(no need for extra code or importing extra libraries)"""

# Set up empty list
history_list = []

# Get five items of data
for item in range(5):
    get_item = input('Enter a number: ')
    history_list.append(get_item)

# Show that everything made it to the list
print()
print('Full list')
print(history_list)

print()
print('Most recent 3')
# print items starting at the end of the list
for item in range(3):
    print(history_list[len(history_list) - item - 1])



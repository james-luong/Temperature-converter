"""Get data from user and store it in a list,
then display the most recent 3 entries
Trial #2 - uses a deque method (no need for reverse ordering)"""

from collections import deque
history_list = deque()

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


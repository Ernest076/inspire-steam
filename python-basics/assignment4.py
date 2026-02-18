# Name : Ernest Matata
# Date: 18th February 2026
# Program to display diamond and triangle pattern using for loops in Python

rows = 7
# Upper part of the diamond
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Lower part of the diamond
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Triangle of stars
for i in range(1, rows + 1):
    print('*' * i)
    


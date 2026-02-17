# Name : Ernest Matata
# Date: 11th February 2026
# Program to demonstrate the use of for loops in Python
import math
for x in range(0,360,30):
     print(math.sin(x))

for x in range(0,360,30):
     print(math.cos(x))

for x in range(0,360,30):
     print(math.tan(x))


for i in range(10,0,-1):
     print(i)

for x in range (0,360,30):
     print(x)

for x in range(-180,180,30):
     print(f"cos({x}) = {math.cos(x)}")

<<<<<<< HEAD
# Triangle of stars
rows = 7
for i in range(1, rows + 1):
    print('*' * i)

# Diamond of stars
rows = 8


# Upper part of the diamond
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

# Lower part of the diamond
for i in range(rows - 2, -1, -1):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))    
=======
print("|")
>>>>>>> 3f2ed30a44d7e3ccc4298d79d838d264e8c89a38

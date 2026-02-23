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

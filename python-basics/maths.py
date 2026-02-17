# Name : Ernest Matata
# Date: 13th February 2026
# Program to perform basic mathematical operations
import math
number = -16.79

print(abs(number)) 


angle_radians = 60
angle_degrees = angle_radians / 180

x = 1
y = math.degrees(x)


print(min(3,4))
print(max(39,46))

print(math.sqrt(144))

print(25**2) # 25 raised to the power of 2
print(3**3) # 3 raised to the power of 3

import math
from tabulate import tabulate

# Angles in degrees
angle = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
# Calculate sine, cosine, and tangent for each angle]
 
# Prepare data
data = []
for angle in angle:
    rad = math.radians(angle)  # Convert angle to radians
    row = [angle, math.sin(rad), math.cos(rad), math.tan(rad)]
    data.append(row)

# Print table
print(tabulate(data, headers=['Angle (degrees)', 'Sine', 'Cosine', 'Tangent']))

import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))   

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"The roots are real and distinct: {root1} and {root2}")
elif d == 0:
    root = -b / (2*a)
    print(f"The roots are real and equal: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"Complex roots:", real_part, "+", imaginary_part, "i and", real_part, "-", imaginary_part, "i")


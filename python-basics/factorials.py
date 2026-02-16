# Name : Ernest Matata
# Date: 16th February 2026
# Program to calculate the factorial of numbers
number = int(input("Enter the number x : "))
factorial = 1 #initialize factorial as 1
for x in range(1, number + 1):
	factorial *= x
print(f"{number}! = {factorial}")


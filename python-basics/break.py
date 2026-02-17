# Name : Ernest Matata
# Date: 17th February 2026
# Program to illustrate break in python

number = 1
while number < 10:
	print(number)
	number += 1
	if number == 4:
		break
	print("breaking from the loop")
	continue
number +=1
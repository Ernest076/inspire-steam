# Name : Ernest Matata
# Date: 13th February 2026
# Program to calculate geometric progression

# Calculating the nth term

a = int(input("Enter the first number :" ))
n = int(input("Enter the number of terms :"))
r = int(input("Enter the common ratio :"))   

nth_term = a * (r ** (n - 1))
sn = a * ((r ** n) - 1) / (r - 1)

print(f"The nth term of the geometric progression is {nth_term}")
print(f"The sum of the first n terms of the geometric progression is {sn}")
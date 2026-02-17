# Name : Ernest Matata
# Date: 17th February 2026
# Program to perform basic arithmetic operations

f_number = 13 # first number
s_number = 50 # second number
sum_numbers = f_number + s_number
diff_numbers = f_number - s_number
product_numbers = f_number * s_number
quotient_numbers = f_number / s_number


print(f"The sum of the numbers %d "% sum_numbers)
print(f"The quotient of the numbers %0.2f "%quotient_numbers)

#modulus - remainder
print(7%5)

# even and odd numbers
for x in range(0,21):
     if( x%2 ==1 ):
           print(f"{x} is an odd number" )
     elif (x%2 == 0):
           print(f"{x} is an even number" )
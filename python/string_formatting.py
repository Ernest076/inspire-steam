# Name: Ernest Matata
# Date: 11th February 2026
# String Formatting

# Get string length
from io import open_code


sentence = "I am learning Python"

string_length = len(sentence) 

print(f"The length of the string is {string_length}")

# Splitting a string
sentence_2 = "Mathematics Chemistry"
split = sentence_2.split(" ")

print(f"the first subject is {split[0]}")


# Make everything uppercase
mpesa_code = "Ii8thyrfg" 


capitalized = mpesa_code.upper()

print("New mpesa code is: ", capitalized)

# Make everything lowercase
mpesa_code = "II8THYRFG"

lowercase = mpesa_code.lower()

print("New mpesa code is: ", lowercase)

# Replacing characters in a string


balance = "100Kes"
amount_added = "900Kes" 


cleaned_balance = balance.replace("Kes", "")

print("Cleaned balance is: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", "")

print("Cleaned amount added is: ", cleaned_amount_added)

total_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"Your new mpesa balance is {total_balance}Kes")
print(f"You have received {cleaned_amount_added}Kes from Kelvin, your new balance is {total_balance}Kes")
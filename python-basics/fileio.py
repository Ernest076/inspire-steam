# Name : Ernest Matata
# Date : 24/02/2026
#Program to perform file operations

#Create new file
new_file = open("student_data.txt","r+")

#Write to new file
new_file.write("{Student Name : Ernest Matata, ID: 27389262 , email :matataernest66@gmail.com}")
new_file.close()

#Read data from the file
new_file = open("Student_data.txt")
data = new_file.read()
print(data)
new_file.close()

#Delete file
#Use OS module
import os
os.remove("remove.txt")

#Delete folder
os.rmdir("folder")
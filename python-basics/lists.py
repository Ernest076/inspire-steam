# Name : Ernest Matata
# Date: 18th February 2026
# Program to show lists in Python
# Lists of friends
Friends = ["Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"]

print(Friends)
Friends.sort()
print(Friends)
Friends.reverse()
print(Friends)
Friends.append("Gunther")
print(Friends)

new_friends = ["Leon", "Benedict", "Clement", "Kimmy", "Sophie"]
print(len(new_friends))

#new list of students
Students = Friends + new_friends

print(Students)
Students.pop()
print(Students)
Students.insert(5,"Makena")
print(Students)

Students.insert(8,"Makori")
print(Students)
Students.extend("Dan")
print(Students)

Students.remove("Gunther")
print(Students)

new_Students = Students.copy()

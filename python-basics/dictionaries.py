# Name : Ernest Matata
# Date : 18th Feb 2026
# Program to show dictionaries in python


car = {"Model" : "Audi",
        "Make" : "A4",
        "Colour" : "Wine",
        "Year" : "2023"}

print(car)

print(car["Model"])
print(car["Year"])

students = {"Alice": 24,
           "James": 18,
          "Mark": 22,
           "Daisy":19}

for key in students:
     print(key)

for val in students.values():
     print(val)

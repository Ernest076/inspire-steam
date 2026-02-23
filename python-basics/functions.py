# Name : Ernest Matata
# Date : 19/02/2026
# Program to demonstrate functions in Python  


def cook_egg():
     pan = True
     heat = True
     eggs = 2
     oil = "20ml"

     print("The pan is {pan}, and the fire is {heat}, \
           add {oil} amount of oil and cook{eggs} eggs")

print("Here is statement 1")

print("Here is statement 2")

cook_egg()

print("Here is statement 3")

     # Ride fare creating function


def create_fare(route, distance, is_rush_hour):

     fare = distance * 10
     if is_rush_hour == True:
          fare = fare * 1.5
     print(f"The fare on route {route}, is (fare)")

     return fare

rush_hour = True
returned_fare = create_fare("Juja-Allsops", 7, rush_hour)
print(f"The fare returned is: {returned_fare}")

# Passing a list as a parameter
def write_all_interests(interests):
     for interest in interests:
            print(f"I am interested in {interest}")

all_interest = ["Bike riding", "Hiking","Researching", "Painting"]

write_all_interests(all_interest)
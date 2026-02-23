# Name : Ernest Matata
# Date : 23/02/2026
# Program to show classes in python

class Car():
    # Attributes of the car
    def __init__(self,model,make,colour,year):
         self.model = model
         self.make =  make
         self.colour = colour
         self.year = year

    # print car details
    def print_details(self,model,make,colour,year):
         print(f"{make}, {model} of colour {colour} was manufactured in the year {year}")



#instantiate a class object

my_car = Car("Discovery 4", "Land Rover", "Midnight blue", "2014")
dads_car = Car("Land Cruiser Prado", "Toyota", "Silver", "2008")

my_car.print_details("Discovery 4", "Land Rover", "Midnight blue", "2014")
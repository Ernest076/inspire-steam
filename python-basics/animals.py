# Name : Ernest Matata
# Date : 23/02/2026
# Program to show inheritance in python

class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight} kgs")

    def eat(self,food):
        print(f"The animal eats {food}")



class Cat(Animal):
    def __init__(self,colour,height,breed):
        super().__init__(self,species,weight,food)
        self.height = height
        self.breed = breed

    def mew(self):
        print(f"Th cat says meow meow")    
    


class Donkey(Animal):
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def brays(self):
        print(f"The donkey says bray bray")
    
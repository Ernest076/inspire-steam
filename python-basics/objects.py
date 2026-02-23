# Name : Ernest Matata
# Date : 19/02/2026
# Classes(objects) in Python

class Human:
     # Define the human being's attributes
     type = "Mammal"
     legs = 2
     brain = True
     warm_blooded = True
     city = "Bujumbura"

     # We then create a constructor for the class object
     # The constructor will be used to create copies of this
     def __init__(self, name, age):
          self.human_name = name
          self.human_age = age

     def tell_story(self):
          print(f"Hello,I am{self.human_name} Here is a story")
          print("There was once a bot that went to Jupiter to get the juzz")

# Create the objects
Ernest = Human("Ernest", 18)
Fetty = Human("Leon", 19)

# Let the humans created do things
Ernest.tell_story()
print("Ernest's age is: ", Ernest.human_age)

# Modify one of the objects, without modifying other objects
Fetty.city = "Atlanta"

print("Fetty's location: ", Fetty.city)
print("Ernest's location: ", Ernest.city)


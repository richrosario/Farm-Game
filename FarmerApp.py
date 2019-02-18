from Farmer import Farmer
from Farm import Farm

print("Welcome to the first day on your new farm!")

day = 0

#creating farm and farmer objects + intros 

newFarm = Farm(input("Want to give your farm a name? "),"none")
newFamer = Farmer(input("What is your name? "),10,10)

print("Welcome " + newFamer.name + " to " + newFarm.name + "!")
print("Day: " + str(day))
newFarm.get_weather()

newFarm.crops = input("You find some seeds in your pocket, what are they? ")

print(newFarm.crops)
print("function in farm class to plant these,reduce hunger")

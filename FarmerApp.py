from Farmer import Farmer
from Farm import Farm

print("Welcome to the first day on your new farm!")

day = 0

#creating farm and farmer objects + intros 

newFarm = Farm(input("Want to give your farm a name? "),"none", "none")
newFarmer = Farmer(input("What is your name? "),10,5)

print("Welcome " + newFarmer.name + " to " + newFarm.name + "!")
print("Day: " + str(day))
newFarm.get_weather()

#starter crop 
newFarm.crops = input("You find some seeds already planted, what are they? ")
newFarm.animals = input("You see some animals in the distance, what are they? ")



#loop of actions while we are not exhausted
while newFarmer.sleep != 0:

	if newFarmer.sleep == 1:
		print("You being to feel very tired, maybe you should sleep")

	else:

		action = input("What would you like to do? \n -Water farm? \n -Feed chickens? \n -Sleep? ").lower()

		if action == "water farm":
			newFarm.water_crops()
			newFarmer.sleep -= 1
		elif action == "feed chickens":
			newFarm.feed_chickens()
			newFarmer.sleep -= 1
		elif action == "sleep":
			newFarmer.sleep()




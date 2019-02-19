import random


class Farm:
	def __init__(self, name, crops,animals):
		self.name = name
		self.crops = crops
		self.animals = animals
		

	def get_weather(self):
		weather = random.randint(1,7)
		if weather == 7:
			print("Rainy day! :( ")
		else:
			print("Sunny day!")

	def water_crops(self):
		print("Your " + self.crops + " look taller after being watered")

	def feed_chickens(self):
		random_egg = random.randint(1,3)
		if random_egg == 1:
			print("You find an egg while feeding your " + self.animals + "!")
		else:
			print("Your " + self.animals + " look happy after being fed!")
import random

class Farm:
	def __init__(self, name, crops):
		self.name = name
		self.crops = crops
		

	def get_weather(self):
		weather = random.randint(1,10)
		if weather == 7:
			print("Rainy day! :( ")
		else:
			print("Sunny day!")
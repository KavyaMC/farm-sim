class Bird:
	def __init__(self,species,gender,cost):
		self.species=species
		self.gender=gender
		self.cost=cost
		self.age=0
		self.isAlive=True
		self.isHungry=False
	def __str__(self):
		status="alive" if self.isAlive else "dead"
		hungry="hungry" if self.isHungry else "full"
		return f"{self.gender}, {self.species}, age:{self.age} {status} {hungry}"
	def age_up(self):
		if self.isAlive:
			self.age+=1
			self.isHungry=True
class Chicken(Bird):
	def __init__(self, gender ):
		super().__init__("chicken",gender,100)

class Duck (Bird):
	def __init__ (self,gender):
		super().__init__("duck",gender,150)
class Turkey(Bird):
	def __init__(selff,gender):
		super().__init__("turkey",gender,300)

class Housing:
	def __init__(self,name,max_capacity):
		self.name=name
		self.max_capacity=max_capacity
		self.occupants=[]
		self.dirt_level=0
	def add_bird(self,new_bird):
		if len(self.occupants)<self.max_capacity:
			self.occupants.append(new_bird)
			print(f"{new_bird} added to {self.name}")
			return True
		else:
			print(f"{self.name} is full")
			return False
	def clean(self):
		self.dirt_level=0
		print(f"{self.name} is clean")
class Player:
	def __init__ (self, name):
		self.name=name
		self.coins=250
		self.properties=[]

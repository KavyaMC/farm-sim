class Bird:
	def __init__(self, species, gender):
		self.species=species
		self.gender=gender
		self.age=0
		self.isAlive=True
		self.isHungry=0
		self.isThirsty=0

	def __str__(self):
		status="alive" if self.isAlive else "dead"
		hungry="hungry" if self.isHungry>=60 else "satiated"
		thirsty="thirsty" if self.isThirsty>=60 else "quenched"
		return (
			f"bird: {self.species} | "
			f"age: {self.age} | "
			f"status: {status} | "
			f"Hunger: {hungry} ({self.isHungry}) | "
			f"thirsty: {thirsty} ({self.isThirsty})"
		)

	def age_up(self):
		if self.isAlive:
			self.age+=1
			self.isHungry=min(100, self.isHungry+10)
			self.isThirsty=min(100, self.isThirsty+10)

	def produce(self):
		if not self.isAlive:
			return 0
		if self.isAlive:
			if self.isHungry<60 and self.isThirsty<60 and self.gender=="female":
				return 1
		return 0

	def eat(self):
		self.isHungry=max(0, self.isHungry-10)

	def eat(self):
		self.isThirsty=max(0, self.isThirsty-10)

class Chicken(Bird):
	def __init__(self, gender ):
		super().__init__("chicken",gender)

class Duck (Bird):
	def __init__ (self,gender):
		super().__init__("duck",gender)

class Turkey(Bird):
	def __init__(self,gender):
		super().__init__("turkey",gender,)

class Building:
	def __init__(self,name,max_capacity):
		self.name=name
		self.max_capacity=max_capacity
		self.occupants=[]
		self.cleanliness=0
		self.produce=0
		self.feed=100
		self.water=100

	def can_add_bird(self,new_bird):
		if len(self.occupants)<self.max_capacity:
			self.occupants.append(new_bird)
			print(f"{new_bird} added to {self.name}")
			return True
		else:
			print(f"{self.name} is full")
			return False

	def feed_level(self):
		if not Bird.isAlive:
			return
		if Bird.isAlive:
			for Bird in self.occupants:
				if self.feed>0:
					bird.eat()
					self.feed-=10

	def water_level(self):
		if not Bird.isAlive:
			return
		if Bird.isAlive:
			for Bird in self.occupants:
				if self.water>0:
					bird.drink()
					self.water-=10

	def dirt_level(self):
		self.dirt_level=0
		print(f"{self.name} is clean")

class Player:
	def __init__ (self, name):
		self.name=name
		self.coins=250
		self.properties=[]

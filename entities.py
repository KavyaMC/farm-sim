import config
class Bird:
	def __init__(self, bird_type, gender):
		if bird_type not in config.BIRD_TYPES:
			raise ValueError("Invalid bird type")

		if gender not in ["male", "female"]:
			raise ValueError("Invalid gender")

		data = config.BIRD_TYPES[bird_type]

		self.bird_type = bird_type
		self.gender = gender

		# pulled from config
		self.housing_type = data["housing"]
		self.produce_item = data["produce"]
		self.age = 0
		self.hunger = 0
		self.thirst = 0
		self.isAlive = True

	def eat(self):
		if not self.isAlive:
			return

		self.hunger = max(self.hunger - 10, 0)

	def drink(self):
		if not self.isAlive:
			return

		self.thirst = max(self.thirst - 10, 0)

	def daily_update(self):
		if not self.isAlive:
			return

		self.age += 1
		self.hunger = min(self.hunger + 10, 100)
		self.thirst = min(self.thirst + 10, 100)

		if self.hunger == 100 or self.thirst == 100:
			self.isAlive = False

	def produce(self, storage):
		if not self.isAlive:
			return

		if self.hunger>50 or self.thirst>50:
			return

		if self.gender != "female":
			return

		item = self.produce_item

		if item not in storage:
			storage[item] = 0
		storage[item] += 1

	def status(self):

		return {
			"type": self.bird_type,
			"gender": self.gender,
			"age": self.age,
			"hunger": self.hunger,
			"thirst": self.thirst,
			"alive": self.isAlive
		}

class Chicken(Bird):
	def __init__(self, gender):
		super().__init__("chicken", gender)

class Duck(Bird):
	def __init__(self, gender):
		super().__init__("duck", gender)

class Turkey(Bird):
	def __init__(self, gender):
		super().__init__("turkey", gender)

class Housing:
	def __init__(self, housing_type):
		if housing_type not in config.HOUSING_TYPES:
			raise ValueError("Invalid housing type")

		data = config.HOUSING_TYPES[housing_type]

		self.housing_type = housing_type
		self.capacity = data["capacity"]
		self.occupants = []
		self.storage = {}
		self.turns_since_clean = 0

	def can_add_birds(self, number):
		if len(self.occupants) + number <= self.capacity:
			return True

		return False

	def add_bird(self, bird):
		if bird.housing_type != self.housing_type:
			raise ValueError("Wrong housing type")

		if not self.can_add_birds(1):
			raise ValueError("Housing full")

		self.occupants.append(bird)

	def feed(self):
		for bird in self.occupants:
			if bird.isAlive:
				bird.eat()

	def water(self):
		for bird in self.occupants:
			if bird.isAlive:
				bird.drink()

	def clean(self):
		self.turns_since_clean = 0

	def needs_cleaning(self):
		if self.turns_since_clean >= 7:
			return True

		return False

	def daily_update(self):
		self.turns_since_clean += 1

		for bird in self.occupants:

			bird.daily_update()

			if bird.isAlive:
				bird.produce(self.storage)

	def status(self):
		return {
			"type": self.housing_type,
			"birds": len(self.occupants),
			"capacity": self.capacity,
			"stored_items": self.storage,
			"needs_cleaning": self.needs_cleaning()
		}

class ChickenCoop(Housing):
	def __init__(self):
		super().__init__("coop")

class DuckPond(Housing):
	def __init__(self):
		super().__init__("pond")

class TurkeyPen(Housing):
	def __init__(self):
		super().__init__("pen")


class Player:
	def __init__(self):
		self.coins = 250
		self.inventory = {}
		self.housings = []

	def add_housing(self, housing):
		self.housings.append(housing)

	def collect_from_housing(self, housing):
		for item in housing.storage:

			if item not in self.inventory:
				self.inventory[item] = 0

			self.inventory[item] += housing.storage[item]
		housing.storage = {}

	def daily_update(self):
		for housing in self.housings:
			housing.daily_update()

	def status(self):
		return {
			"name": self.name,
			"coins": self.coins,
			"inventory": self.inventory,
			"housing_count": len(self.housings)
		}
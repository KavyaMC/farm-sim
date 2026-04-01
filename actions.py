import random
import config
from entities import Housing, Chicken, Duck, Turkey

def buy_housing(player, housing_choice):
	data = config.HOUSING_TYPES[str(housing_choice)]
	price = data["buy_price"]

	if player.coins < price:
		return False, "Insufficient funds."

	new_house = Housing(data["name"], data["capacity"])
	player.housings.append(new_house)
	player.coins -= price
	return True, f"Bought {data['name']}. Balance: {player.coins}"


def buy_bird(player, bird_choice, house_choice):
	if len(player.housings) == 0:
		return False, "Buy housing first."

	bird_data = config.BIRD_TYPES[str(bird_choice)]
	price = bird_data["buy_price"]
	species = bird_data["name"]
	bird_class = globals()[bird_data["class_name"]]

	if player.coins < price:
		return False, f"Insufficient funds. Balance: {player.coins}"

	target_house = player.housings[house_choice - 1]
	if species not in target_house.name.lower():
		return False, "Wrong housing type."

	gender = random.choice(["male", "female"])
	new_bird = bird_class(gender)
	success = target_house.add_bird(new_bird)

	if not success:
		return False, "Housing full."

	player.coins -= price
	return True, f"Bought {gender} {species}. Balance: {player.coins}"


def sell_house(player, house_index):
	house = player.housings[house_index - 1]
	if len(house.occupants) > 0:
		return False, "House must be empty to sell."

	player.housings.pop(house_index - 1)
	return True, f"Sold {house.name}."


def sell_bird(player, house_index, bird_index):
	house = player.housings[house_index - 1]
	bird = house.occupants.pop(bird_index - 1)

	if isinstance(bird, Chicken):
		price = config.BIRD_TYPES["1"]["sell_price"]
	elif isinstance(bird, Duck):
		price = config.BIRD_TYPES["2"]["sell_price"]
	else:
		price = config.BIRD_TYPES["3"]["sell_price"]

	player.coins += price
	return True, f"Sold bird for {price} coins. Balance: {player.coins}"


def sell_produce(player, item_name, amount):
	if item_name not in player.storage or player.storage[item_name] < amount:
		return False, "Not enough produce."

	price = config.PRODUCE_TYPES.get(item_name, {"sell_price": 5})["sell_price"]
	total = price * amount

	player.storage[item_name] -= amount
	if player.storage[item_name] == 0:
		del player.storage[item_name]

	player.coins += total
	return True, f"Sold {amount} {item_name} for {total} coins. Balance: {player.coins}"
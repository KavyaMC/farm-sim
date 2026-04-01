import os
import json
from entities import *
import config


SAVE_FOLDER = "slots"

def ensure_save_folder():
	if not os.path.exists(SAVE_FOLDER):
		os.makedirs(SAVE_FOLDER)

def get_filename(slot_number, player_name="empty"):
	ensure_save_folder()
	return os.path.join(SAVE_FOLDER, f"slot{slot_number}_{player_name}.txt")

def check_save_exists():
	ensure_save_folder()
	for i in range(1, 5):
		found = False
		for f in os.listdir(SAVE_FOLDER):
			if f.startswith("slot" + str(i) + "_"):
				found = True
				break
		if found:
			return True
	return False

def save_game(slot_number):
	player = config.active_player
	if player == "":
		print("No active player to save.")

		return

	filename = get_filename(slot_number, player.name)
	data = {
		"name": player.name,
		"coins": player.coins,
		"housings": []
	}

	for house in player.housings:
		h_data = {
			"type": house.housing_type,
			"turns_since_clean": house.turns_since_clean,
			"storage": {},
			"birds": []
		}
		for item, count in house.storage.items():
			h_data["storage"][item] = count
		for bird in house.occupants:
			b_data = {
				"bird_type": bird.bird_type,
				"gender": bird.gender,
				"age": bird.age,
				"hunger": bird.hunger,
				"thirst": bird.thirst,
				"isAlive": bird.isAlive
			}
			h_data["birds"].append(b_data)
		data["housings"].append(h_data)

	with open(filename, "w") as f:
		json.dump(data, f, indent=4)

	print(f"Game saved to {filename}")
	return "main menu"

def load_game(slot_number):
	ensure_save_folder()
	files = []
	for f in os.listdir(SAVE_FOLDER):
		if f.startswith("slot" + str(slot_number) + "_"):
			files.append(f)
	if not files:
		print("No save file in this slot.")
		return False

	filename = os.path.join(SAVE_FOLDER, files[0])
	with open(filename, "r") as f:
		data = json.load(f)

	player = Player()
	player.name = data.get("name", "empty")
	player.coins = data.get("coins", 250)

	for h in data.get("housings", []):
		h_type = h.get("type")
		if h_type == "coop":
			house_obj = ChickenCoop()
		elif h_type == "pond":
			house_obj = DuckPond()
		elif h_type == "turkey_pen":
			house_obj = TurkeyPen()
		else:
			continue
		house_obj.turns_since_clean = h.get("turns_since_clean", 0)
		house_obj.storage = {}
		for item, count in h.get("storage", {}).items():
			house_obj.storage[item] = count
		for b in h.get("birds", []):
			b_type = b.get("bird_type")
			gender = b.get("gender")
			if b_type == "chicken":
				bird_obj = Chicken(gender)
			elif b_type == "duck":
				bird_obj = Duck(gender)
			elif b_type == "turkey":
				bird_obj = Turkey(gender)
			else:
				continue
			bird_obj.age = b.get("age", 0)
			bird_obj.hunger = b.get("hunger", 0)
			bird_obj.thirst = b.get("thirst", 0)
			bird_obj.isAlive = b.get("isAlive", True)
			house_obj.occupants.append(bird_obj)
		player.housings.append(house_obj)

	config.active_player = player
	print(f"Game loaded from {filename}")
	return True

def delete_game(slot_number):
	ensure_save_folder()
	files = []
	for f in os.listdir(SAVE_FOLDER):
		if f.startswith("slot" + str(slot_number) + "_"):
			files.append(f)
	
	if not files:
		print("No save file in this slot.")
		return "main menu"
	
	for f in files:
		os.remove(os.path.join(SAVE_FOLDER, f))
		print(f"Deleted {f}")
	return "main menu"
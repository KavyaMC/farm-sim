import os
from entities import *
import random

active_player = None
active_house = None

def status_screen():
	global active_player
	print(f"Status. Balance: {active_player.coins}")
	if len(active_player.properties)==0:
		print("You don't have any properties")
		return "ranchmenu"
	for index, house in enumerate(active_player.properties,start=1):
		print(f"{index}. {house.name} capacity: {len(house.occupants)}/{house.max_capacity} dirt: {house.dirt_level}")
		if len(house.occupants)>0:
			for occupant in house.occupants:
				print(occupant)

		else:
			print("no occupants")

		print()
	return "ranchmenu"

def manage_house_menu():
	global active_player
	global active_house

	if len(active_player.properties) == 0:
		print("No housing available.")
		return "ranchmenu"

	for index, house in enumerate(active_player.properties,start=1):
		print(f"{index}. {house.name}. dirt level: {house.dirt_level}")
	cancel=len(active_player.properties)+1
	print(f"{cancel}. go back")
	choice=input("select an option").strip()
	if choice.isdigit():
		choice=int(choice)
		if choice==cancel:
			return "ranchmenu"
		if 1 <= choice <= len(active_player.properties):
			active_house = active_player.properties[choice-1]
			return "specifichousemenu"
	else:
		print("invalid choice")
	return "managehousemenu"

def manage_specific_house():
	global active_house
	global active_player

	if active_house is None:
			print("No house selected.")
	return "managehousemenu"

	print(f"{active_house.name}.")
	print("1. Feed")
	print("2. water")
	print("3. clean")
	print("4. move to storage.")
	print("5. storage")
	print("6. go back")
	choice=input("select an option").strip()
	match choice:
		case "1":
			print("in development")

		case "2":
			print("in development")
		case "3":
			active_house.clean()
			return "managehousemenu"
		case "6":
			return "managehousemenu"
		case _:
			print("invalid choice")
	return "managehousemenu"

def buy_housing():
	global active_player
	print("1. chicken coop.")
	print("2. duck pond")
	print("3. turkey pen")
	print("4. go back")
	choice=input("select an option").strip()
	match choice:
		case "1":
			house_name="chicken coop"
			house_capacity=15
			house_price=80

		case "2":
			house_name="duck pond"
			house_capacity=15
			house_price=120

		case "3":
			house_name="turkey pen"
			house_capacity=15
			house_price=150

		case "4":
			return "buymenu"

		case _:
			print("invalid choice")
			return "buymenu"

	if active_player.coins >= house_price:
		active_player.coins -= house_price

		new_house = Housing(house_name, house_capacity)
		active_player.properties.append(new_house)
		print(f"bought {house_name}, balance: {active_player.coins}")
	else:
		print("insufficient funds")
		return "buymenu"

	return "buymenu"

def buy_birds():
	global active_player

	print("1. buy chicken")
	print("2. buy duck")
	print("3. buy turkey")
	print("4. go back")

	choice = input("select an option").strip()

	match choice:
		case "1":
			bird_name="chicken"
			bird_class=Chicken
			bird_price=100

		case "2":
			bird_name="duck"
			bird_class=Duck
			bird_price=150

		case "3":
			bird_name="turkey"
			bird_class=Turkey
			bird_price=200

		case "4":
			return "buymenu"

		case _:
			print("invalid choice")
			return "buymenu"

	if len(active_player.properties) == 0:
		print("Buy housing first")
		return "buymenu"

	if active_player.coins < bird_price:
		print(f"insufficient funds. Balance:{active_player.coins}")
		return "buymenu"

	gender = random.choice(["male","female"])
	new_bird = bird_class(gender)

	print("Select housing:")
	for index, house in enumerate(active_player.properties, start=1):
		print(f"{index}. {house.name}")
	choice = input("Select housing: ").strip()
	if not choice.isdigit():
		print("invalid choice")
		return "buymenu"
	choice = int(choice)

	if choice < 1 or choice > len(active_player.properties):
		print("invalid choice")
		return "buymenu"

	target_house = active_player.properties[choice - 1]	

	if bird_name not in target_house.name:
		print("wrong housing type")
		return "buymenu"

	success = target_house.add_bird(new_bird)
	if success:
		active_player.coins -= bird_price
		print(f"bought {gender} {bird_name}. Balance: {active_player.coins}")
	else:
		print("buy additional unit of housing")
	return "buymenu"

def buy_menu():
	global active_player
	print("1. buy housing")
	print("2. buy birds")
	print("3. go back.")
	choice=input("select an option").strip()
	match choice:
		case "1":
			return "buyhousingmenu"
		case "2":
			return "buybirdsmenu"
		case "3":
			return "ranchmenu"
		case _:
			print("invalid choice")
	return "ranchmenu"


def check_save_exists():
	if (os.path.exists("slot1.txt") or 
		os.path.exists("slot2.txt") or 
		os.path.exists("slot3.txt") or 
		os.path.exists("slot4.txt")):
		return True
	return False

def save_game(slot_number, player_name):
	filename = f"slot{slot_number}.txt"

	with open(filename, "w") as file:
		file.write(f"name:{active_player.name}\n")
		file.write(f"coins:{active_player.coins}\n")

		for house in active_player.properties:
			file.write(f"house:{house.name},{house.max_capacity},{house.dirt_level}\n")

	print(f"Game successfully saved to {filename}.")
def delete_menu():
	for i in range(1,5):
		print(f"{i}. slot {i}.txt")
	print("5. cancel")
	choice=input("select an option").strip()
	if choice=="5":
		return "mainmenu"
	if choice in ["1","2","3","4"]:
		filename=f"slot{choice}.txt"
		print(f"Would you like to delete {filename}")
		choice=input("select y/n")
		if choice=="y":
			try:
				os.remove(filename)
				print("successfully deleted the file")

			except FileNotFoundError:
				print("the file is already deleted")
			return "mainmenu"
		else:
			print(f"{filename} was not deleted")
			return "mainmenu"
	else:
		print("invalid choice")
		return "mainmenu"
def main_menu():
	has_save = check_save_exists()
	print("Main Menu ")
	if has_save:
		print("1. Continue")
		print("2. Save")
		print("3. Delete")
		print("4. Help")
		print("5. Credits")
		print("6. Exit")
	else:
		print("1. New Game")
		print("2. Help")
		print("3. Credits")
		print("4. Exit")

	choice = input("Please choose an option: ").strip()

	if has_save:
		match choice:
			case "1":
				print("Select slot to load")
				print("1. Slot 1")
				print("2. Slot 2")
				print("3. Slot 3")
				print("4. Slot 4")
				slot = input("Select slot: ").strip()
				if slot in ["1","2","3","4"]:
					success = load_game(slot)
					if success:
						return "agriculturemenu"
				return "mainmenu"
			case "2": return "saveslotmenu"
			case "3": 
				return "deletemenu"

			case "4": 
				print("This is a farm simulator.")
				return "mainmenu"
			case "5": 
				print("Designed buy Kavya.")
				return "mainmenu"
			case "6": return "exit"
			case _:
				print("Invalid choice.")
				return "mainmenu"
	else:
		match choice:
			case "1": return "saveslotmenu"
			case "2": 
				print("This is a farm simulator.")
				return "mainmenu"
			case "3": 
				print("Designed by Kavya.")
				return "mainmenu"
			case "4": return "exit"
			case _:
				print("Invalid choice.")
				return "mainmenu"

def save_slot_menu():
	global active_player

	if active_player is None:
		print(" Save Slot Selection ")
		name = input("Enter your name: ")
		active_player = Player(name)

	print("1. Slot 1")
	print("2. Slot 2")
	print("3. Slot 3")
	print("4. Slot 4")

	slot = input("Select a slot: ").strip()

	match slot:
		case "1": save_game("1", active_player.name)
		case "2": save_game("2", active_player.name)
		case "3": save_game("3", active_player.name)
		case "4": save_game("4", active_player.name)
		case _:
			print("Invalid choice.")
			return "saveslotmenu"
	return "mainmenu"

def load_game(slot_number):
	global active_player

	filename = f"slot{slot_number}.txt"

	try:
		with open(filename, "r") as file:
			lines = file.readlines()

		player_name = ""
		player_coins = 0
		active_player = None

		for line in lines:

			# Safe split
			parts = line.strip().split(":")

			if len(parts) != 2:
				continue

			key, value = parts

			if key == "name":
				player_name = value
				active_player = Player(player_name)

			elif key == "coins":
				player_coins = int(value)

				if active_player is not None:
					active_player.coins = player_coins

			elif key == "house":
				name, capacity, dirt = value.split(",")

				new_house = Housing(name, int(capacity))
				new_house.dirt_level = int(dirt)

				if active_player is not None:
					active_player.properties.append(new_house)

		if active_player is None:
			print("Load failed: player data missing.")
			return False

		print(f"Loaded player: {player_name}")
		return True

	except FileNotFoundError:
		print("Save file not found.")
		return False
def agriculture_menu():
	print(" Agriculture Building")
	print("1. Ranch")
	print("2. Cropland")
	print("3. Go to main menu")
	choice = input("Select an option: ").strip()

	match choice:
		case "1": return "ranchmenu"
		case "2": return "cropland"
		case "3": return "mainmenu"
		case _:
			print("Invalid choice.")
			return "agriculturemenu"

def ranch_menu():
	global active_player
	if active_player is None:
		print("No player loaded.")
		return "mainmenu"

	menu_items=["Buy","sell","housing","storage","status","End turn","go back"]
	print("The Ranch ")
	for index, item in enumerate(menu_items,start=1):
		print(str(index)+"."+item)
	choice = input("Select an option: ").strip()

	match choice:
		case "1": return "buymenu"
		case "2":
			print("Sell system in development.")
			return "ranchmenu"
		case "3":
			return "managehousemenu"
		case "4":
			print("In development.")
			return "ranchmenu"
		
		case "5":
			return "statusscreen"

		
		case "6":
			for house in active_player.properties:
				house.dirt_level += random.randint(1, 3)
			print("Turn ended.")
			return "ranchmenu"

		case "7": return "agriculturemenu"
		case _:
			print("Invalid choice.")
			return "ranchmenu"

current_state = "mainmenu"
print("Welcome to Farm Simulator!")
while current_state != "exit":
	match current_state:
		case "mainmenu":
			current_state = main_menu()
		case "saveslotmenu":
			current_state = save_slot_menu()
		case "agriculturemenu":
			current_state = agriculture_menu()
		case "ranchmenu":
			current_state = ranch_menu()
		case "cropland":
			print("Cropland is under development.")
			current_state = "agriculturemenu"
		case "deletemenu":
			current_state=delete_menu()
		case "buymenu":
			current_state=buy_menu()
		case "buyhousingmenu":
			current_state=buy_housing()
		case "buybirdsmenu":
			current_state=buy_birds()
		case "statusscreen":
			current_state=status_screen()
		case "managehousemenu":
			current_state=manage_house_menu()
		case "specifichousemenu":
			current_state=manage_specific_house()
		case _:
			print("Unknown State.")
			current_state = "exit"


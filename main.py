import os
from entities import *
import random
def sell_menu():
	global active_player
	print("1. Sell birds.")
	print("2. sell eggs.")
	print("3. sell house.")
	print("4. go back")
	choice=input("select an option")
	match choice:
		case "1":
			return "sellbirdsmenu"
		case "2":
			print("in development")
		case "3":
			return "sellhousemenu"
		case "4":
			return "ranchmenu"
		case _:
			print("invalid choice")
			return "sellmenu"

def sell_house_menu():
	global active_player
	for index,house in enumerate(active_player.properties,start=1):
		print (f"{index}. {house.name} contains {len(house.occupants)}")
	cancel=len(active_player.properties)+1

	print(f"{cancel}. go back")
	building_choice=input("select an option")
	if building_choice==cancel:
		return "sellmenu"
	if building_choice.isdigit() and 1<= int(building_choice) <= len(active_player.properties):
		building_choice=int(building_choice)
		target_house=active_player.properties[building_choice-1]

		if len(target_house.occupants)>0:
			print(f"{target_house.name} is not empty, so it can't be sold")
			return "sellmenu"
		else:
			active_player.properties.pop(building_choice-1)
			print(f"successfully sold {target_house.name}")
			return "sellmenu"
	else:
		print("invalid choice")
		return "sellmenu"


def status_screen():
	global active_player
	print(f"Status. Balance: {active_player.coins}")
	if len(active_player.properties)==0:
		print("You don't have any properties")
		return "ranchmenu"
	for index, house in enumerate(active_player.properties,start=1):
		print(f"{index}. {house.name} capacity: {len(house.occupants)}/{house.max_capacity}")
		if len(house.occupants)>0:
			for occupant in house.occupants:
				print(occupant)

		else:
			print("no occupants")
	return "ranchmenu"
def manage_house_menu():
	global active_player
	global active_house
	for index, house in enumerate(active_player.properties,start=1):
		print(f"{index}. {house.name}. dirt level: {house.dirt_level}")
	cancel=len(active_player.properties)+1
	print(f"{cancel}. go back")
	choice=input("select an option")
	if choice.isdigit():
		if choice==cancel:
			return "ranchmenu"
		active_house=active_player.properties[int(choice)-1]
		return "specifichousemenu"
	else:
		print("invalid choice")
	return "ranchmenu"
def manage_specific_house():
	global active_house
	global active_player
	print(f"{active_house.name}.")
	print("1. Feed")
	print("2. water")
	print("3. clean")
	print("4. move to storage.")
	print("5. storage")
	print("6. go back")
	choice=input("select an option")
	match choice:
		case "1":
			print("in development")

		case "2":
			print("in development")
		case "3":
			active_house.clean()
		case "6":
			return "managehousemenu"
		case _:
			print("invalid choice")
	return "managehousemenu"

def buy_housing():
	global active_player
	print("1. chicken coop.")
	print("2. go back")
	choice=input("select an option")
	match choice:
		case "1":
			if active_player.coins>=80:
				active_player.coins-=80
				chicken_coop=Housing("Chicken coop",15)
				active_player.properties.append(chicken_coop)
				print(f"Bought chicken coop. Balance: {active_player.coins}")
			else:
				print("insufficient funds")
		case "2":
			return "buymenu"
		case _:
			print("invalid choice")
	return "buymenu"

def buy_birds():
	global active_player
	print("1. buy chicken")
	print("2. go back")
	choice=input("select an option")
	match choice:
		case "1":
			if active_player.coins>=100:
				if len(active_player.properties)==0:
					print("buy housing first")
					return "buymenu"
				active_player.coins-=100
				gender=random.choice(["male","female"])
				new_chicken=Chicken(gender)
				target_house=active_player.properties[0]
				success=target_house.add_bird(new_chicken)
				if success:
					print(f"bought {gender} chicken. Balance: {active_player.coins}")
				else:
					print("buy more housing")
					active_player.coins+=100
					print(f"Balance:{active_player.coins}")
			else:
				print(f"insufficient funds. Balance:{active_player.coins}")
		case "2":
			return "buymenu"
		case _:
			print("invalid choice")
	return "buymenu"

def buy_menu():
	global active_player
	print("1. buy housing")
	print("2. buy birds")
	print("3. go back.")
	choice=input("Select an option")
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
		file.write(player_name)
	print(f"Game successfully saved to {filename}.")
def delete_menu():
	for i in range(1,5):
		print(f"{i}. slot {i}.txt")
	print("5. cancel")
	choice=input("select an option")
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
			case "1": return "agriculturemenu"
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
				print("Designed buy Kavya.")
				return "mainmenu"
			case "4": return "exit"
			case _:
				print("Invalid choice.")
				return "mainmenu"

def save_slot_menu():
	print(" Save Slot Selection ")
	name = input("Enter your name: ")
	print("1. Slot 1")
	print("2. Slot 2")
	print("3. Slot 3")
	print("4. Slot 4")
	slot = input("Select a slot: ").strip()

	match slot:
		case "1": save_game("1", name)
		case "2": save_game("2", name)
		case "3": save_game("3", name)
		case "4": save_game("4", name)
		case _:
			print("Invalid choice.")
			return "saveslotmenu"
	return "agriculturemenu"

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
	menu_items=["Buy","sell","housing","storage","status","End turn","go back"]
	print("The Ranch ")
	for index, item in enumerate(menu_items,start=1):
		print(str(index)+"."+item)
	choice = input("Select an option: ").strip()

	match choice:
		case "1":
			
			return "buymenu"
		case "2":
			return "sellmenu"
		case "3":
			return "managehousemenu"
		case "4":
			print("In development.")
			return "ranchmenu"
		
		case "5":
			return "statusscreen"

		
		case "6":
			print("In development.")
			return "ranchmenu"
		
		
		case "7": return "agriculturemenu"
		case _:
			print("Invalid choice.")
			return "ranchmenu"

current_state = "mainmenu"
print("Welcome to Farm Simulator!")
name=input("enter your name")
active_player=Player(name)
active_house=None
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
		case "sellmenu":
			current_state=sell_menu()
		case "sellhousemenu":
			current_state=sell_house_menu()
	
		case _:
			print("Unknown State.")
			current_state = "exit"


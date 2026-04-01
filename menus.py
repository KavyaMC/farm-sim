import config
from actions import *
from save_system import *
from entities import Player
import random
import sys


# ---------- Utility Functions ----------
def display_menu(title, options):
	print(f"\n{title}")

	for idx, item in enumerate(options, start=1):
		print(f"\t{idx}. {item}")

	choice = input("Select an option: ").strip()

	if not choice.isdigit():
		print("Invalid input.")

		return None

	choice = int(choice)

	if not 1 <= choice <= len(options):
		print(f"Enter a number between 1 and {len(options)}.")

		return None

	return choice


def pause():
	input("Press Enter to continue...")


# ---------- Menus ----------
def manage_specific_house():
    house = config.active_house
    if house == "":
        print("No house selected.")
        pause()
        return "manage house menu"

    options = ["Feed", "Water", "Clean", "Move to storage", "Go back"]
    choice = display_menu(house.name, options)
    if choice is None:
        return "specific house menu"

    match choice:
        case 1 | 2 | 4:
            print("In development.")
            pause()
            return "specific house menu"
        case 3:
            house.clean()
            pause()
            return "manage house menu"
        case 5:
            config.active_house = ""
            return "manage house menu"

    return "specific house menu"


def manage_house_menu():
    player = config.active_player
    if player == "" or len(player.properties) == 0:
        print("No housing available.")
        pause()
        return "ranch menu"

    options = [f"{house.name} | Dirt level: {house.dirt_level}" for house in player.properties]
    options.append("Go back")

    choice = display_menu("Select Housing", options)
    if choice is None:
        return "manage house menu"

    if choice == len(options):
        return "ranch menu"

    config.active_house = player.properties[choice - 1]
    return "specific house menu"


def sell_menu():
    options = ["Sell birds", "Sell eggs", "Sell house", "Go back"]
    choice = display_menu("Sell Menu", options)
    if choice is None:
        return "sell menu"

    match choice:
        case 1:
            return "sell birds menu"
        case 2:
            return "sell produce menu"
        case 3:
            return "sell house menu"
        case 4:
            return "ranch menu"

    return "sell menu"


def buy_menu():
    options = ["Buy housing", "Buy birds", "Go back"]
    choice = display_menu("Buy Menu", options)
    if choice is None:
        return "buy menu"

    match choice:
        case 1:
            return "buy housing menu"
        case 2:
            return "buy birds menu"
        case 3:
            return "ranch menu"

    return "buy menu"


def ranch_menu():
    player = config.active_player
    if player == "":
        print("No player loaded.")
        pause()
        return "main menu"

    options = ["Buy", "Sell", "Housing", "Storage", "Status", "End turn", "Go back"]
    choice = display_menu("Ranch Menu", options)
    if choice is None:
        return "ranch menu"

    match choice:
        case 1:
            return "buy menu"
        case 2:
            return "sell menu"
        case 3:
            return "manage house menu"
        case 4:
            print("In development.")
            pause()
            return "ranch menu"
        case 5:
            return "status screen"
        case 6:
            for house in player.properties:
                house.dirt_level += random.randint(1, 3)
            print("Turn ended.")
            pause()
            return "ranch menu"
        case 7:
            return "agriculture menu"

    return "ranch menu"


def agriculture_menu():
    options = ["Ranch", "Cropland", "Back to Main Menu"]
    choice = display_menu("Agriculture Building", options)
    if choice is None:
        return "agriculture menu"

    match choice:
        case 1:
            return "ranch menu"
        case 2:
            print("Cropland is under development.")
            pause()
            return "agriculture menu"
        case 3:
            return "main menu"

    return "agriculture menu"


def delete_menu():
    options = ["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Cancel"]
    choice = display_menu("Delete Save Slot", options)
    if choice is None:
        return "delete menu"
    if choice == 5:
        return "main menu"
    result = delete_game(choice)
    pause()
    return result


def save_slot_menu():
    if config.active_player == "":
        name = input("Enter your name: ").strip()
        if name == "" or not name.isalpha():
            print("Name cannot be empty.")
            pause()
            return "save slot menu"
        config.active_player = Player()
        config.active_player.name = name
        print(f"Player created: {name}")
        pause()

    choice = display_menu("Choose Save Slot", ["Slot 1", "Slot 2", "Slot 3", "Slot 4"])
    if choice is None:
        return "save slot menu"

    save_game(choice)
    pause()
    return "main menu"


def main_menu():
    has_save = check_save_exists()

    if has_save:
        options = ["Continue", "Save", "Delete", "Help", "Credits", "Exit"]
    else:
        options = ["New Game", "Help", "Credits", "Exit"]

    choice = display_menu("Main Menu", options)
    if choice is None:
        return "main menu"

    if has_save:
        match choice:
            case 1:
                slot = display_menu("Load Slot", ["Slot 1", "Slot 2", "Slot 3", "Slot 4"])
                if slot is None:
                    return "main menu"
                if load_game(str(slot)):
                    print(f"Player {config.active_player.name} loaded.")
                    pause()
                    return "agriculture menu"
                return "main menu"
            case 2:
                return "save slot menu"
            case 3:
                return "delete menu"
            case 4:
                print("This is a farm simulator.")
                pause()
                return "main menu"
            case 5:
                print("Designed by Kavya.")
                pause()
                return "main menu"
            case 6:
                print("Thank you for playing. Exiting program")
                pause()
                sys.exit()
    else:
        match choice:
            case 1:
                return "save slot menu"
            case 2:
                print("This is a farm simulator.")
                pause()
                return "main menu"
            case 3:
                print("Designed by Kavya.")
                pause()
                return "main menu"
            case 4:
                print("Thank you for playing. Exiting program")
                pause()
                sys.exit()

    return "main menu"
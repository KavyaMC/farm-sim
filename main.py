from menus import *
from save_system import delete_game
current_state = "main menu"
print("Welcome to Farm Simulator!")
while not current_state=="exit":
	match current_state:
		case "main menu":
			current_state = main_menu()
		case "save slot menu":
			current_state = save_slot_menu()
		case "agriculture menu":
			current_state = agriculture_menu()
		case "ranch menu":
			current_state = ranch_menu()
		case "cropland menu":
			print("Cropland is under development.")
			pause()
			current_state = "agriculture menu"
		case "delete menu":
			current_state=delete_menu()
		case "buy menu":
			current_state=buy_menu()
		case "buy housing menu":
			current_state=buy_housing()
		case "buy birds menu":
			current_state=buy_bird()
		case "sell menu":
			current_state = sell_menu()
		case "sell birds menu":
			current_state = sell_bird()
		case "sell produce menu":
			current_state = sell_produce()
		case "sell housing menu":
			current_state = sell_house()
		case "status screen":
			current_state=status_screen()
		case "manage house menu":
			current_state=manage_house_menu()
		case "specific house menu":
			current_state=manage_specific_house()
		case _:
			print("Unknown State.")
			current_state = "exit"
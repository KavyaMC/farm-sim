config={
	"coins": 250,
	"save_slots": 4,
	"birds": {

		"chicken": {
			"male": "Rooster",
			"female": "Hen",
			"cp": 100,
			"sp": 60,
			"produce": "chicken eggs",
			"buildings": "chicken coop"
		},
		"duck": {
			"male": "Drake",
			"female": "Duck",
			"cp": 150,
			"sp": 90,
			"produce": "duck eggs",
			"building": "duck pond"
		},
		"turkey": {
			"male": "Tom",
			"female": "Hen",
			"cp": 300,
			"sp": 165,
			"produce": "turkey meat",
			"building": "turkey pen"
		}
	},
	"buildings": {
		"capacity": 15,
		"chicken_coop": {"cp": 80, "sp": 40},
		"duck_pond": {"cp": 125, "sp": 62},
		"turkey_pen": {"cp": 200, "sp": 100}
	},
}

def get_bird(species):
	return config["birds"][species]

def get_price(species):
	return CONFIG["birds"][species]["price"]
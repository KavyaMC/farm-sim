active_player=""
active_house=""
current_slot=""

BIRD_TYPES = {

	"1": {
		"name": "chicken",
		"class_name": "Chicken",
		"buy_price": 100,
		"sell_price": 50,
		"produce": "chicken eggs",
		"housing": "chicken coop"
	},

	"2": {
		"name": "duck",
		"class_name": "Duck",
		"buy_price": 150,
		"sell_price": 75,
		"produce": "duck eggs",
		"housing": "duck pond"
	},

	"3": {
		"name": "turkey",
		"class_name": "Turkey",
		"buy_price": 300,
		"sell_price": 150,
		"produce": "turkey meat",
		"housing": "turkey pen"
	}

}

HOUSING_TYPES = {

	"1": {
		"name": "chicken coop",
		"species": "chicken",
		"capacity": 15,
		"buy_price": 80,
		"sell_price": 50
	},

	"2": {
		"name": "duck pond",
		"species": "duck",
		"capacity": 15,
		"buy_price": 140,
		"sell_price": 90
	},

	"3": {
		"name": "turkey pen",
		"species": "turkey",
		"capacity": 15,
		"buy_price": 250,
		"sell_price": 175
	}

}

PRODUCE_TYPES = {

	"chicken eggs": {
		"name": "chicken eggs",
		"sell_price": 25
	},

	"duck eggs": {
		"name": "duck eggs",
		"sell_price": 45
	},

	"turkey meat": {
		"name": "turkey meat",
		"sell_price": 90
	}

}

PLAYER_DEFAULTS = {
	"name": "",
	"starting_coins": 250,
	"storage": {},
	"housing": [],
	"birds": {}
}
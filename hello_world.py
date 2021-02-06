favorite_numbers = {
	'ante': {
		'numbers': [2,5,13,20],
	},
	'lucy': {
		'numbers': [32,18,4,5],
	},
	'carla': {
		'numbers': [0,11,55,28],
	},
}

for name, number in favorite_numbers.items():
	print(f"\nName: {name.title()}")
	print(f"\n\tYour favorite numbers are: {number['numbers']}")

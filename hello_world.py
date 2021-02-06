cities = {
	'rio de janeiro': {
		'country': 'brazil',
		'population': '6.5 million',
		'fact': 'Rio de Janeiro means January River, but the river is actually a bay',
	},
	'moscow': {
		'country': 'russia',
		'population': '12.7 million',
		'fact': 'Moscow claims the largest number of billionaires in the world. Per Forbes, there are 84 billionaires in the city',
	},
	'tokyo': {
		'country': 'japan',
		'population': '9.2 million',
		'fact': ' Tokyo is the largest metropolitan in the world, hosting over 36 million people spread over 3 prefectures.',
	},
}

for city,city_info in cities.items():
	print(f"\nName of the city: {city.title()}")
	print(f"\n\t{city.title()} is city places in {city_info['country'].title()} with population {city_info['population']}.")
	print(f"\n\t{city_info['fact']}.")

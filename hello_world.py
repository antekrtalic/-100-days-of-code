class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.name} with {self.type} cuisine type.")

    def open_restaurant(self):
        print("Restaurant is open!")

restaurant = Restaurant('Mirazur', 'fine-dining')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Noma', 'casual dining')
restaurant.describe_restaurant()

restaurant = Restaurant('Asador Etxebarri', 'fast-casual')
restaurant.describe_restaurant()

restaurant = Restaurant('Gaggan', 'fast food')
restaurant.describe_restaurant()

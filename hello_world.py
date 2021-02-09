class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name} with {self.cuisine_type} cuisine type.")
        print(f"Restaurant has served {self.number_served} customers!")

    def open_restaurant(self):
        print("Welcome, restaurant is open!")

    def set_number_served(self, customers):
       self.number_served = customers

    def increment_number_served(self, increment):
        self.number_served += increment
restaurant = Restaurant('Maslina', 'bistro')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(3)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.increment_number_served(6)
restaurant.describe_restaurant()
restaurant.open_restaurant()

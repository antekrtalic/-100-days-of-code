class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print("\n***USERS INFORMATION***")
        print(f"\nFirst name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"\nHello {self.first_name}! How are you?")


user = User('Ante', 'Dragoje', 25, 'Zagreb')
user.describe_user()
user.greet_user()

user = User('Monika', 'Dragoje', 22, 'Zagreb')

user.describe_user()
user.greet_user()

user = User('Mirta', 'Didara', 42, 'Osijek')

user.describe_user()
user.greet_user()

user = User('Igor', 'Jedvaj', 19, 'Varaždin')

user.describe_user()
user.greet_user()

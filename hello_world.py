class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print("\n***SUMMARY OF USER'S INFORMATIONS***")
        print(f"\nFirst name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"\nHello {self.first_name}!It's good to see you.")

    def increment_login(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Ante', 'Dragoje', 25, 'Mostar')
user.describe_user()

user.increment_login()
user.increment_login()
user.increment_login()
user.increment_login()
user.increment_login()
print(f"Logging attempt so far: {user.login_attempts}")
user.reset_login_attempts()
print(f"Logging attempt so far: {user.login_attempts}")

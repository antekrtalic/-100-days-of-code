filename = "guest.txt"

with open(filename, "a") as file_object:
    x = 0
    while x in range(3):
        user = input("What is your name? ")
        print(f"Welcome {user}")
        file_object.write(f"{user}\n")
        print(f"You were successfully added in the {filename}")
        x += 1

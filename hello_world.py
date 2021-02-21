filename = "responses.txt"

with open(filename, "a") as file_object:
    x = 0
    while x in range(3):
        user = input("Why do you like programming so much? ")
        file_object.write(f"{user}\n")
        x += 1

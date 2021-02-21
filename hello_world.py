filename = "cat.txt"
dog_file = "dog.txt"

try:
    with open(filename, "a") as file_object:
        for x in range(3):
            user = input("Enter cat's name ")
            file_object.write(f"{user}\n")

    with open(filename) as file_objectt:
        for line in file_objectt:
            print(line.strip())

    with open(dog_file, "a") as dog_object:
        for x in range(3):
            user = input("Enter dog's name ")
            dog_object.write(f"{user}\n")

    with open(dog_file) as dog_object:
        for dog in dog_object:
            print(dog.strip())

except FileNotFoundError:
    print("File not found!")

filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    message = line
    print(message.replace("functions", "class"))
    print(message.replace("OOP", "POO"))

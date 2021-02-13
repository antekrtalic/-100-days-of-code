def list_manipulation(arry, command, location, value):
    if command == "add" and location == "beginning":
        return [value] + arry

print(list_manipulation([1,2,3], "add", "beginning", 20))

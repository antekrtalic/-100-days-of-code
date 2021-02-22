import json

def add_num():
    """Storing favorite num inside json file"""
    filename = "favorite_number.json"
    user_num = input("What is your favorite num?\n ")
    
    with open(filename, 'w') as f:
        json.dump(user_num, f)


def read_num():
    """Reading favorite number"""
    filename = "favorite_number.json"
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return f"I know your favorite number! It's {number}."

def new_num():
    """Adding new number"""
    filename = 'favorite_number.json'
    user_num = input("What number do you want to add?\n ")
    with open(filename) as f:
        read = json.load(f)

    if user_num in read:
        return f"That number is already in {filename}"
    else:
        with open(filename, "a") as f:
            json.dump(user_num, f)
            return f"We store your number {user_num}"
add_num()
print(read_num())
print(new_num())

import random

random_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10"))

while guess != random_number:
    guess = int(input("Guess a number between 1 and 10"))
    too_low = random_number - guess
    too_high = guess - random_number
    if too_low >= 1:
        print("Too low, try again!")
    elif too_high >= 1:
        print("Too high, try again!")
    if guess == random_number:
        print("You guessed it!You won!")
        ask = input("Do you want to keep playing? (y/n)")
        if ask == "y":
            random_number = random.randint(1, 10)
            guess = int(input("Guess a number between 1 and 10"))
        elif ask == "n":
            break
        else:
            print("You type wrong answer")
            ask = input("Do you want to keep playing? (y/n)")

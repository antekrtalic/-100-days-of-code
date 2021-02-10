from random import choice
from random import choices

lottery = ["M", "A", 3, 11, 15, 26, 18, 19, 4, 2, 55, 63, "R", "L"]
prize_combination = []

while len(prize_combination) != 4:
    current = choice(lottery)
    prize_combination.append(current)

print(f"This is prize combination: {prize_combination}")

my_ticket = []
count = 0

while my_ticket != prize_combination:
    my_ticket = choices(lottery, k=4)
    count += 1

if my_ticket == prize_combination:
    print(f"You win first prize! It took you {count} guesses:")
    print(my_ticket, prize_combination)

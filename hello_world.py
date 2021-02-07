restaurant_seating = input("How many people are there in your dinner group?")
restaurant_seating = int(restaurant_seating)

if restaurant_seating > 8:
    print("\nYou'll have to wait for the table.")
else:
    print("\nTable is ready.")

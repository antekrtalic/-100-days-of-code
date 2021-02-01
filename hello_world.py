names = ["john", "alen", "floria", "sim", "eva"]

name = "Alen"

if name.lower() in names:
	print(f"This is your name {name}.")
else:
	print("We didn't find your name.")


name = "Sofia"

if name.lower() not in names:
	print(f"We didn't find {name}.")
else:
	print("There she is.")

current_users = ["natasha", "john", "eric", "lora", "jacob", "math"]

new_users = ["john", "natasha", "philip", "asta", "eric", "samantha"]

for new_user in new_users:
	if new_user in current_users:
		print(f"Username {new_user} was already used!")
	else:
		print(f"Username {new_users} is available.")

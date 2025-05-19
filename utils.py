class MenuOptionError(Exception):
	pass

def print_users(users_list):
	print("Here is the list of users")
	for index, user in enumerate(users_list):
		print(f"{index} - {user["users"]}")
	pass

def print_passwords(password_list):
	print("Here is a list of passwords")
	for index, password in enumerate(passwords_list):
		print(f"{index} - {password["password"]}")
	pass

def format_error(error_message):
	print("\n#### ERROR ###")
	print(error_message)
	print("###############\n")

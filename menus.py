import functions
import utils

def main_menu():
	try:
		print("===MENU===")
		print("1 - Print users")
		print("2 - Print passwords")
		choices = input("Select option 1 or 2: ")
		if choices not in ["1", "2"]:
			raise utils.MenuOptionError
		return int(choices)
	except utils.MenuOptionError:
		utils.format_error("Option not valid.")

def back_to_main_menu():
	input("Press any key and return to main menu...")

def print_users_menu(users_list): # the parameter comes from the utils.py file
	print("\n=====USERS DATABASE===")
# missing functions.print_users()
	functions.print_users(users_list)
	print("========================\n")
	back_to_main_menu()

def print_passwords_menu(passwords_list):
	print("\n====PASSWORDS====")
# missing functions.print_passwords()
	functions.print_passwords(passwords_list)
	print("===================\n")
	back_to_main_menu()

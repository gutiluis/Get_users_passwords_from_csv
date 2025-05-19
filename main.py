import csv
import menus


if __name__ == "__main__":
	user_list = []
	password_list = []
	with open("file.csv", newline="") as csvfile:
		reader = csv.DictReader(csvfile, delimiter=",")
		for row in reader:
			user_list.append({
				"user": row["user_name"]
			})
			password_list.append({
				"password": row["password"]
			})
	menu_choices = 0
	while menu_choices != 4:
		menu_choices = menus.main_menu()
		if menu_choices == 1:
# make function inside menus.py file for the print_user()
			menus.print_users_menu(user_list)
		if menu_choices == 2:
			menus.print_passwords_menu(password_list)
	print("End of loop")

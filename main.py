import random


characters = list("abcedfghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789" + "!@#^5$£&()][}{")

def generate_random_password():
	length = int(input("Enter password length: "))
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("password:", "".join(password))


generate_random_password()
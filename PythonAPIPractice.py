import requests

class User:
	def __init__(self, first_name, last_name, email):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

	def welcome(self):
		print(f"Loaded profile of user {self.first_name} {self.last_name}!")

	def getEmail(self):
		print(f"Users email is: {self.email}")

def main():
	lookupUserByName()





def singleUser():

	URL = "https://reqres.in/api/users/2"

	data = getData(URL)

	data = data['data']
	first_name = data['first_name']
	email = data['email']
	last_name = data['last_name']

	janet = User(first_name, last_name, email)

	janet.welcome()
	janet.getEmail()


def populateMultipleUsers():
	URL = "https://reqres.in/api/users?page=2"
	users = []

	data = getData(URL)

	data = data['data']


	for i in data:

		for key, value in i.items():
			if key == 'first_name':
				first_name = value
			if key == 'last_name':
				last_name = value
			if key == 'email':
				email = value

		users.append(User(first_name, last_name, email))

	return users

def greetAllUsers():
	users = populateMultipleUsers()

	for i in users:
		i.welcome()
		i.getEmail()
		print()

def lookupUserByName():
	users = populateMultipleUsers()

	

	response = input("Would you like to see a directory? y/n\n")

	deciding = True

	while deciding:
		if response == "y":
			for i in users:
				print(i.first_name)
				deciding = False
		elif response == "n":
			deciding = False
		else:
			response = input("Invalid response. y/n\n")


	first_name = input("Enter their first name:\n")

	for i in users:
		if i.first_name == first_name:
			print("Great! We found them! :D")
			i.welcome()
			i.getEmail()

	

def getData(URL):
    r = requests.get(url = URL)
    return r.json()

if __name__ == "__main__":
	main()

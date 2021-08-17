import requests



class User:
	def __init__(self, first_name, last_name, email):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

	def welcome(self):
		print(f"Hello {first_name} {last_name}!")

	def getEmail(self):
		print(f"Your email is: {email}")


URL = "https://reqres.in/api/users/2"

r = requests.get(url = URL)

data = r.json()

# email
# first name
# last name
data = data['data']

first_name = data['first_name']
email = data['email']
last_name = data['last_name']




janet = User(first_name, last_name, email)

janet.welcome()
janet.getEmail()




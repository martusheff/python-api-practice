import requests

URL = "https://reqres.in/api/users/2"

userId = 2

PARAMS = {'id' : userId}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

# email
# first name
# last name
email = data['data']['email']

print(email)

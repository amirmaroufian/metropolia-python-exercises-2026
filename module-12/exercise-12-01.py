import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

if response.status_code == 200:
    joke = response.json()
    print(joke["value"])
else:
    print("Failed to fetch joke.")
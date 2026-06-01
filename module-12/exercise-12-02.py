import requests

api_key = "a1b2c3d4e5f67890abcdef1234567890"

municipality = input("Enter municipality: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    description = data["weather"][0]["description"]
    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15

    print(f"Weather: {description}")
    print(f"Temperature: {temperature_celsius:.1f} °C")
else:
    print("Municipality not found.")
import requests
import os

# set the envvar API_KEY before run this code
API_KEY = os.environ['API_KEY']
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    wheater = data['weather'][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Wheater:", wheater)
    print("Temperature:", temperature, "celsius")
else:
    print("An error ocurred.")

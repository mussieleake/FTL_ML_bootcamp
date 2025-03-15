import requests

API_KEY = "010858a3a88847f1a4154131242207"
URL = "http://api.weatherapi.com/v1/current.json"

city = input("Enter the city name to get current weather data: ")
params = {
    "key": API_KEY,
    "q": city
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    current = data.get("current", {})
    condition = current.get("condition", {}).get("text", "No condition info")
    temperature_c = current.get("temp_c", "N/A")

    print("\nWeather Data:")
    print(f"City: {city}")
    print(f"Temperature (C): {temperature_c}")
    print(f"Condition: {condition}")
else:
    print("Failed to retrieve weather data. Please check the city name and try again.")

class Weather:
    def __init__(self, city, temperature, condition):
        self.city = city
        self.temperature = temperature
        self.condition = condition

    def __str__(self):
        return (f"Weather in {self.city}:\n"
                f"Temperature (C): {self.temperature}\n"
                f"Condition: {self.condition}")

if response.status_code == 200:
    weather_obj = Weather(city, temperature_c, condition)
    print("\nUsing the Weather class:")
    print(weather_obj)
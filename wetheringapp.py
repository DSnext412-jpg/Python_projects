import requests

API_KEY = "83661a6be81f480cac885734262305 "

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

else:
    print("City not found or invalid API key")

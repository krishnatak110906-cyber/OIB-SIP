import requests, os
from dotenv import load_dotenv
load_dotenv()

def get_weather(city="Delhi"):
    key = os.getenv("WEATHER_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    data = requests.get(url, params={"q":city,"appid":key,"units":"metric"}).json()

    if "main" not in data:
        return "City not found"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"{city} temperature is {temp} degree Celsius with {desc}"

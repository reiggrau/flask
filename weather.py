from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import sys

load_dotenv()


def get_current_weather(city="Barcelona"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Current Weather Conditions ***\n")

    city = input("Please enter a city name:\n")

    # Check for empty strings or empty spaces
    if not bool(city.strip()):
        city = 'Barcelona'  # Default

    weather_data = get_current_weather(city)

    pprint(weather_data)

    # Handle city not found
    if not weather_data['cod'] == 200:
        sys.exit("There was an error!")

    print(f"\nCurrent weather for: {weather_data['name']}")
    print(f"The sky is: {weather_data['weather'][0]['description']}")
    print(f"The temperature is: {weather_data['main']['temp']} °C")
    print(f"The humidity is: {weather_data['main']['humidity']} %")

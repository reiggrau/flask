from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Barcelona"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Current Weather Conditions ***\n")

    city = input("Please enter a city name:\n")

    weather_data = get_current_weather(city)
# Install Flask
# 1 - Create an environment
# py -3 -m venv .venv
#
# 2 - Activate the environment
# source .venv/Scripts/activate
#
# 3 - Install Flask
# pip install Flask

from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

# Define routes


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or empty spaces
    if not bool(city.strip()):
        city = 'Barcelona'  # Default

    weather_data = get_current_weather(city)

    # Check for city not found
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title=weather_data['name'],
        weather=f"{weather_data['weather'][0]['description']}".capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        humidity=weather_data['main']['humidity']
    )

# Local
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)

# To deploy app
# pip install waitress
# pip freeze > requirements.txt


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

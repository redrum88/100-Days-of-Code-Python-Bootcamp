import requests
import time
import os
from twilio.rest import Client

power = True
# Weather API
KEY = os.environ.get("KEY_TOKEN")        # Openweathermap KEY
URL = "https://api.openweathermap.org/data/2.5/forecast/"  # URL Address


# Parameters dict
PARAMETERS = {
    "appid": KEY,
    "q": "Dudley",      # City where you live
    "units": "metric"
}

# SMS API

account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"      # Twilio SID
auth_token = os.environ.get("AUTH_TOKEN")         # Twilio Auth Key
client = Client(account_sid, auth_token)

will_rain = False
text_msg = ""


def check_weather():
    global will_rain, text_msg
    response = requests.request(url=URL, params=PARAMETERS, method="GET")
    response.raise_for_status()
    data = response.json()
    city = data["city"]["name"]
    population = data["city"]["population"]
    temp = data["list"][1]["main"]["temp"]
    weather = data["list"][1]["weather"][0]["main"]
    weather_id = data["list"][1]["weather"][0]["id"]
    time1 = data["list"][1]["dt_txt"]
    msg = f"Take an umbrella!!!\nTime: {time1}\nTemperature: {round(temp)}°C\nWeather: {weather}\nCity: {city}\nPopulation: {population}\n "

    if weather_id > 700:
        will_rain = True
        text_msg = msg


def send_msg():
    message = client.messages \
        .create(
        body=text_msg,
        from_='+14258421421',       # Enter your Twilio Phone Number
        to='+44xxxxxxxx'          # Enter your Phone Number
    )
    print(message.sid)


while power:
    check_weather()
    if will_rain:
        send_msg()

    time.sleep(3600)

import requests
from datetime import datetime

GENDER = "Male"     # Your gender
WEIGHT_KG = 70      # Your Weight in kilograms
HEIGHT_CM = 180     # Your Height in centimeters
AGE = 40            # Your Age in years

API_ID = "Your API ID"     # Your API ID
API_KEY = "Your API KEY"    # Your API KEY
USERNAME = "Your Username"        # Your Username
PASSWORD = "Your Password"       # Your Password

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "LINK TO YOU SHEETY"

question = input("Tell me which exercise you did: ")

HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
AUTH = (
    USERNAME,
    PASSWORD
)

PARAMETERS = {
    "query": question,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=PARAMETERS, headers=HEADERS)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for question in result["exercises"]:
    add_to_sheet = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": question["name"].title(),
            "duration": question["duration_min"],
            "calories": question["nf_calories"]

        }
    }
    sheet_response = requests.post(
        url=sheety_endpoint,
        json=add_to_sheet,
        auth=AUTH
    )
    print(sheet_response.text)

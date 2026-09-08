import requests
from datetime import datetime
# import os

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

APP_ID = "ADC"
API_KEY = "ABC"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(response.text)
# print(result["exercises"][0]["name"])

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

########################################################################################################################
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = "https://api.sheety.co/65cdd5ff1a1fd6fe235220fa1127230a/workoutTracking/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json= sheet_inputs)
# print(sheet_response.text)

#     # Sheety Authentication Option 1: No Auth
#     """
#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#     """
#
#     # Sheety Authentication Option 2: Basic Auth
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         auth=(
#             os.environ["ENV_SHEETY_USERNAME"],
#             os.environ["ENV_SHEETY_PASSWORD"],
#         )
#     )
#
#     # Sheety Authentication Option 3: Bearer Token
#     """
#     bearer_headers = {
#         "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
#     }
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         headers=bearer_headers
#     )
#     """
#     print(f"Sheety Response: \n {sheet_response.text}")

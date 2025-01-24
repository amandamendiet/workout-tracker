from dotenv import load_dotenv
import os
import requests
from datetime import *

load_dotenv()

NUTRI_APP_ID = "7f208c68"
NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/1bfb2d6e09148818451627bf99059c65/workoutTracker/workouts"
SHEETY_USERNAME = "amandamendiet"
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")

NUTRI_HEADERS = {
    'x-app-id':NUTRI_APP_ID,
    'x-app-key':NUTRI_API_KEY,
}
SHEETY_HEADERS = {
    'Authorization':f"Basic {SHEETY_TOKEN}"
}
exercise_entry = input("Tell me about your workout today: ")
nutri_parameters = {
    'query':exercise_entry,
}
nutri_response = requests.post(url=NUTRI_ENDPOINT, headers=NUTRI_HEADERS, json=nutri_parameters)
print(nutri_response.json())

for exercise in nutri_response.json()['exercises']:
    sheety_parameters = {
        'workout':{
            'date':datetime.now().strftime('%d/%m/%Y'),
            'time':datetime.now().strftime('%X'),
            'exercise':exercise['user_input'],
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories'],
            }
        }
    print(sheety_parameters)
    sheety_response = requests.post(url=SHEETY_ENDPOINT,json=sheety_parameters, headers=SHEETY_HEADERS)
    print(sheety_response.text)

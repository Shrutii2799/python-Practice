# import os
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "link to openweathermap api"
api_key = "ABC"
account_sid = "ABcd "
auth_token ="EFG"
weather_params = {
    "lat": -8.597081,
    "lon": 116.100487,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    #
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="phone number",
        to="phone number"
    )
    print(message.status)
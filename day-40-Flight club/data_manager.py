import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):

        self._user = "your_sheety_username"
        self._password = "your_sheety_password"

        self.prices_endpoint = "https://api.sheety.co/xxxxxxx/flightDeals/prices"
        self.users_endpoint = "https://api.sheety.co/xxxxxxx/flightDeals/users"

        self.destination_data = {}
        self.customer_data = {}


    def get_destination_data(self):

        response = requests.get(url=self.prices_endpoint)
        data = response.json()

        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

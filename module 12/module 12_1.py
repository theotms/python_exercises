# Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here:
# https://api.chucknorris.io/. The user should only be shown the joke text.

import json
import requests

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request)

if response.status_code == 200:
    json_response = response.json()
    joke_text = json_response.get("value")
    print (joke_text)

else:
    print("No jokes for u")

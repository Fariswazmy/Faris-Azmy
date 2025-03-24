import json
import requests

name = input("Enter the type of app you want to search for in the app store: ")
response = requests.get(
    "https://itunes.apple.com/search?term=" + name + "&entity=software&limit=10"
)

data = response.json()

if "results" in data:
    for result in data["results"]:
        print("* " + result["trackName"], end=" made by ")
        print(result["sellerName"])
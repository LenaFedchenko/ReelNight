import requests, os, json
from config import API_KEY

title = "Avatar"
def api_request(enter_text= None):
    print(f"____{enter_text}______")
    response: dict = requests.get(f"http://www.omdbapi.com/?t={enter_text}&apikey={API_KEY}").json()
    path = os.path.abspath(os.path.join(__file__, "..", "..", "static", "json", "cinema.json"))
    with open(path, mode= "w") as file:
        json.dump(response, file, indent= 4, ensure_ascii= False)
    return response






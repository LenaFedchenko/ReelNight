import requests
from config import API_KEY
title = "Avatar"
def api_request():
    print(requests.get(f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}").json())
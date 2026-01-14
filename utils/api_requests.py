import requests, os, json
from config import API_KEY


def api_request():
    path = os.path.abspath(os.path.join(__file__, "..", "..", "static", "json", "json_watch.json"))
    with open(path) as file:
        films = json.load(file)
    return films

def search_film(name_film):
    path = os.path.abspath(os.path.join(__file__, "..", "..", "static", "json", "json_watch.json"))
    with open(path) as file:
        films = json.load(file)
    for title in films:
        if title["title"].lower() == name_film:
            return title
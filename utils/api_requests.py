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
        if name_film == title["title"].lower():
            rank = title["rank"]
            return title, rank

def filter(genre_enter):
    list_of_genres = []
    list_ranks = []
    path = os.path.abspath(os.path.join(__file__, "..", "..", "static", "json", "json_watch.json"))
    with open(path) as file:
        films = json.load(file)
    for film in films:
        if genre_enter in film["genre"]:
            list_of_genres.append(film["image"])
            list_ranks.append(film["rank"])
    return list_ranks
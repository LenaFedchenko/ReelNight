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




# def test_movie():
#     url = "https://imdb-top-100-movies.p.rapidapi.com/"

#     headers = {
#         "x-rapidapi-key": "ff08d868e3mshc7a3ad6ea016423p170943jsnb7cf9f189635",
#         "x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers).json()

#     path = os.path.abspath(os.path.join(__file__, "..", "..", "static", "json", "json_watch.json"))
#     with open(path, mode= "w") as file:
#         json.dump(response, file, indent= 4, ensure_ascii= False)
#     return response


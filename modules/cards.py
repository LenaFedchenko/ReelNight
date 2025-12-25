import PyQt6.QtWidgets as widgets
from PIL import Image
# class for change from pil to qt
from PIL.ImageQt import ImageQt
import requests, random
import PyQt6.QtGui as gui
from utils import api_request
from io import BytesIO

films = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Godfather Part II",
    "The Dark Knight",
    "12 Angry Men",
    "Schindler's List",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Lord of the Rings: The Fellowship of the Ring",
    "Forrest Gump",
    "Inception",
    "Fight Club",
    "The Lord of the Rings: The Two Towers",
    "Star Wars: Episode IV - A New Hope",
    "The Matrix",
    "Goodfellas",
    "One Flew Over the Cuckoo's Nest",
    "Se7en",
    "Seven Samurai",
    "It's a Wonderful Life",
    "Interstellar",
    "Parasite",
    "Spirited Away",
    "The Green Mile",
    "Saving Private Ryan",
    "The Silence of the Lambs",
    "City of God",
    "Life Is Beautiful",
    "The Usual Suspects",
    "Léon: The Professional",
    "The Lion King",
    "Back to the Future",
    "Gladiator",
    "Terminator 2: Judgment Day",
    "The Prestige",
    "The Departed",
    "Whiplash",
    "The Intouchables",
    "The Pianist",
    "Joker",
    "Avengers: Endgame",
    "Avengers: Infinity War",
    "Iron Man",
    "Captain America: Civil War",
    "Spider-Man: No Way Home",
    "The Dark Knight Rises",
    "Batman Begins",
    "The Batman",
    "Batman Returns",
    "Man of Steel",
    "Wonder Woman",
    "Aquaman",
    "Dune",
    "Blade Runner",
    "Blade Runner 2049",
    "Alien",
    "Aliens",
    "The Terminator",
    "Jurassic Park",
    "The Matrix Reloaded",
    "The Matrix Revolutions",
    "Mad Max: Fury Road",
    "The Wolf of Wall Street",
    "Titanic",
    "The Social Network",
    "La La Land",
    "The Grand Budapest Hotel",
    "No Country for Old Men",
    "There Will Be Blood",
    "Once Upon a Time in Hollywood",
    "The Hateful Eight",
    "Django Unchained",
    "Kill Bill: Vol. 1",
    "Kill Bill: Vol. 2",
    "Inglourious Basterds",
    "Shutter Island",
    "The Irishman",
    "Casino",
    "Heat",
    "Scarface"
]

def cadrs(third_frame, third_frame_layout, row, name_film: None):
    if name_film == None:
        try:
            info = api_request(random.choice(films))
        except:
            info = api_request("avatar")
    elif name_film != None:
        try:
            info = api_request(name_film)
        except Exception as error:
            print(error)
    response = requests.get(info["Poster"])
    image_bytes = BytesIO(response.content)
    # load our picture
    poster = Image.open(image_bytes)
    # changed picture for PQt6
    qt_poster = ImageQt(poster)
    label3 = widgets.QLabel(parent= third_frame)
    pixmap2 = gui.QPixmap(gui.QImage(qt_poster))
    pixmap2 = pixmap2.scaled(200, 309)
    label3.setPixmap(pixmap2)
    third_frame_layout.addWidget(label3, 1, row)

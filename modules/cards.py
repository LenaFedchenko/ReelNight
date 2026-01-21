import PyQt6.QtWidgets as widgets
from PIL import Image
# class for change from pil to qt
from PIL.ImageQt import ImageQt
import requests, random
import PyQt6.QtGui as gui
from utils import api_request, search_film
from io import BytesIO
import PyQt6.QtCore as core
import os
import webbrowser
from .frames import Frame
from .load_image import ImageLoad
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

def cadrs(third_frame, third_frame_layout, row, name_film):
    if name_film == None:
        info = api_request()
        index = random.randint(0, 99)
        response = requests.get(info[index]["image"])
    elif name_film != None:
        info, index = search_film(name_film= name_film)
        if info:
            response = requests.get(info["image"])
            index = index - 1
        elif info is None:
            info = api_request()
            index = random.randint(0, 99)
            response = requests.get(info[index]["image"])
    image_bytes = BytesIO(response.content)
    poster = ImageLoad(width=200, height=309, bytes_img= image_bytes, frame= third_frame, frame_layout= third_frame_layout, row=1, col= row)
    return index

def info_btn(third_frame, third_frame_layout, row,frame, index_poster):
    info_btn = widgets.QPushButton(third_frame)
    info_btn.setStyleSheet("background-color: none; border-radius: 5px")
    info_btn.setFixedSize(200, 309)
    third_frame_layout.addWidget(info_btn, 1, row)
    info_btn.clicked.connect(lambda: test(frame, index_poster))
    return index_poster

def test(frame, index_poster):
    # Модальне вікно
    MODAL = widgets.QWidget(parent = frame)
    
    MODAL_LAYOUT = widgets.QVBoxLayout()
    MODAL_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
    MODAL_LAYOUT.setContentsMargins(25, 25, 25, 25)
    MODAL_LAYOUT.setSpacing(20)
    MODAL.setLayout(MODAL_LAYOUT)
    colors = ["051727", "15112A", "212832", "393430"]
    color = random.choice(colors)
    MODAL.setStyleSheet(f"border-radius: 16px; background-color: #{color}")
    
    MODAL.setGeometry(
        (1200 // 2) - 426, 
        (800 // 2) - 340, 
        853, 
        680
    )
    
    # HEADER
    HEADER_FRAME_LAYOUT = widgets.QHBoxLayout()
    HEADER_FRAME = Frame(parent= MODAL, width=800, height= 70, layout= HEADER_FRAME_LAYOUT)    
    HEADER_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignRight)
    # HEADER_FRAME_LAYOUT.setSpacing(10)

    image_logo = Image.open(os.path.abspath(os.path.join(__file__, "..", "..", "images", "logo.png")))
    # changed picture for PQt6
    qt_image = ImageQt(image_logo)
    label2 = widgets.QLabel(parent= HEADER_FRAME)
    pixmap = gui.QPixmap(gui.QImage(qt_image))
    pixmap = pixmap.scaled(200, 50)
    label2.setPixmap(pixmap)
    HEADER_FRAME_LAYOUT.addWidget(label2)
    
    CLOSE_BTN = widgets.QPushButton(parent = HEADER_FRAME)
    
    close_icon = gui.QIcon()
    close_icon.addFile(os.path.abspath(os.path.join(__file__, "..", "..", "images", "close.png")))
    
    CLOSE_BTN.setIcon(close_icon)
    CLOSE_BTN.setFixedSize(core.QSize(36, 36))
    CLOSE_BTN.setStyleSheet("border: transparent; ")
    CLOSE_BTN.setCursor(gui.QCursor(core.Qt.CursorShape.PointingHandCursor))
    CLOSE_BTN.clicked.connect(MODAL.hide)
    
    HEADER_FRAME_LAYOUT.addWidget(CLOSE_BTN)
    MODAL_LAYOUT.addWidget(HEADER_FRAME)
    
    
    # CENTER
    CENTER_FRAME_LAYOUT = widgets.QVBoxLayout()
    CENTER_FRAME = Frame(parent= MODAL, width=816, height= 540, layout= CENTER_FRAME_LAYOUT)    
    MODAL_LAYOUT.addWidget(CENTER_FRAME)


    MAIN_INFO_LAYOUT = widgets.QHBoxLayout()
    MAIN_INFO = Frame(parent= CENTER_FRAME, width=800, height= 247, layout= MAIN_INFO_LAYOUT)
    MAIN_INFO_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
    CENTER_FRAME_LAYOUT.addWidget(MAIN_INFO)

    IMG_FRAME_LAYOUT = widgets.QHBoxLayout()
    IMG_FRAME = Frame(parent= MAIN_INFO, width=168, height= 247, layout= IMG_FRAME_LAYOUT)
    IMG_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
    MAIN_INFO_LAYOUT.addWidget(IMG_FRAME)
    info = api_request()
    response = requests.get(info[index_poster]["image"])
    image_bytes = BytesIO(response.content)
    img_poster = ImageLoad(width=145, height=232, frame= IMG_FRAME, frame_layout= IMG_FRAME_LAYOUT, bytes_img= image_bytes)

    DESCRIPTION_LAYOUT = widgets.QVBoxLayout()
    DESCRIPTION = Frame(parent= MAIN_INFO, width=620, height= 226, layout= DESCRIPTION_LAYOUT)
    MAIN_INFO_LAYOUT.addWidget(DESCRIPTION)
    NAME_LAYOUT = widgets.QHBoxLayout()
    NAME = Frame(parent= MAIN_INFO, width=588, height= 70, layout= NAME_LAYOUT)
    DESCRIPTION_LAYOUT.addWidget(NAME)
    GENRE_LAYOUT = widgets.QHBoxLayout()
    GENRE = Frame(parent= MAIN_INFO, width=588, height= 80, layout= GENRE_LAYOUT)
    GENRE_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
    DESCRIPTION_LAYOUT.addWidget(GENRE)

    name_film_get = info[index_poster]["title"]
    top_film_get = info[index_poster]["id"]
    name_film = widgets.QLabel(parent= NAME, text= f"{name_film_get}")
    top_film = widgets.QLabel(parent= NAME, text= f"{top_film_get}")
    name_film.setStyleSheet("""
                            font-size: 40px;
                            color: white
                            """)
    top_film.setStyleSheet("""
                            font-size: 20px;
                            color: white
                            """)
    genres = info[index_poster]["genre"]
    for genre in genres:
        btn = widgets.QPushButton(NAME, text= genre)
        btn.setFixedSize(110, 36)
        btn.setStyleSheet("background-color: #1D1E26; border-radius: 10px; color: white; font-size: 16px")
        GENRE_LAYOUT.addWidget(btn)
    NAME_LAYOUT.addWidget(name_film)
    NAME_LAYOUT.addWidget(top_film)


    INFO_LAYOUT = widgets.QVBoxLayout()
    INFO = Frame(parent= CENTER_FRAME, width=800, height= 181, layout= INFO_LAYOUT)
    INFO_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
    CENTER_FRAME_LAYOUT.addWidget(INFO)
    name_film_get2 = info[index_poster]["title"]
    name_film2 = widgets.QLabel(parent= INFO, text= f"{name_film_get2}")
    name_film2.setStyleSheet("""
                        font-size: 32px;
                        color: white
                        """)
    INFO_LAYOUT.addWidget(name_film2)
    rating = info[index_poster]["rating"]
    rating_get = widgets.QLabel(parent= INFO, text= f"rating: {rating}")
    rating_get.setStyleSheet("""
                        font-size: 20px;
                        color: white
                        """)
    INFO_LAYOUT.addWidget(rating_get)
    year = info[index_poster]["year"]
    year_get = widgets.QLabel(parent= INFO, text= f"year: {year}")
    year_get.setStyleSheet("""
                        font-size: 20px;
                        color: white
                        """)
    INFO_LAYOUT.addWidget(year_get)
    description = info[index_poster]["description"]
    description_get = widgets.QLabel(parent= INFO, text= f"{description}")
    description_get.setWordWrap(True)
    description_get.setStyleSheet("""
                        font-size: 20px;
                        color: white;
                        """)
    INFO_LAYOUT.addWidget(description_get)

    WATCH_BTN_LAYOUT = widgets.QVBoxLayout()
    WATCH_BTN = Frame(parent= CENTER_FRAME, width=800, height= 70, layout= WATCH_BTN_LAYOUT)
    WATCH_BTN_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
    watch_btn = widgets.QPushButton(parent= WATCH_BTN, text= "Watch")
    watch_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    watch_btn.setStyleSheet("""
                            background-color: #FFC6ED;
                            border-radius: 10px;
                            color: black;
                            font-size: 24px;
                            font-weight: 800;
                            """)
    watch_btn.setFixedSize(300, 53)
    CENTER_FRAME_LAYOUT.addWidget(WATCH_BTN)
    WATCH_BTN_LAYOUT.addWidget(watch_btn)
    link = info[index_poster]["imdb_link"]
    watch_btn.clicked.connect(lambda: open_imdb(link))
    MODAL.show()


def open_imdb(link):
    webbrowser.open(f"{link}")
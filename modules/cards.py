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

def cadrs(third_frame, third_frame_layout, row, name_film):
    if name_film == None:
        info = api_request()
        index = random.randint(0, 99)
        response = requests.get(info[index]["image"])
    elif name_film != None:
        info = search_film(name_film= name_film)
        if info:
            response = requests.get(info["image"])
        elif info is None:
            info = api_request()
            index = random.randint(0, 99)
            response = requests.get(info[index]["image"])
    image_bytes = BytesIO(response.content)
    poster = Image.open(image_bytes)
    qt_poster = ImageQt(poster)
    label3 = widgets.QLabel(parent= third_frame)
    pixmap2 = gui.QPixmap(gui.QImage(qt_poster))
    pixmap2 = pixmap2.scaled(200, 309)
    label3.setPixmap(pixmap2)
    third_frame_layout.addWidget(label3, 1, row)
    

def info_btn(third_frame, third_frame_layout, row,frame):
    info_btn = widgets.QPushButton(third_frame)
    info_btn.setStyleSheet("background-color: none; border-radius: 5px")
    info_btn.setFixedSize(200, 309)
    third_frame_layout.addWidget(info_btn, 1, row)
    info_btn.clicked.connect(lambda: test(frame))
def test(frame):
    # Модальне вікно
    MODAL = widgets.QWidget(parent = frame)
    
    MODAL_LAYOUT = widgets.QVBoxLayout()
    MODAL_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
    MODAL_LAYOUT.setContentsMargins(25, 25, 25, 25)
    MODAL_LAYOUT.setSpacing(20)
    MODAL.setLayout(MODAL_LAYOUT)
    colors = ["242E31", "0D53CA", "0D1114", "77685B"]
    color = random.choice(colors)
    MODAL.setStyleSheet(f"border-radius: 16px; background-color: #{color}")
    
    MODAL.setGeometry(
        (1200 // 2) - 426, 
        (800 // 2) - 320, 
        853, 
        640
    )
    
    # HEADER
    HEADER_FRAME = widgets.QFrame(parent = MODAL)
    HEADER_FRAME.setFixedSize(800, 70)
    HEADER_FRAME_LAYOUT = widgets.QHBoxLayout()
    HEADER_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignRight)
    HEADER_FRAME_LAYOUT.setSpacing(10)
    HEADER_FRAME.setLayout(HEADER_FRAME_LAYOUT)
    HEADER_FRAME.setStyleSheet("background-color: green")

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
    CENTER_FRAME = widgets.QFrame(parent = MODAL)
    CENTER_FRAME.setFixedSize(816, 500)
    
    CENTER_FRAME_LAYOUT = widgets.QVBoxLayout()
    CENTER_FRAME_LAYOUT.setSpacing(10)
    CENTER_FRAME.setLayout(CENTER_FRAME_LAYOUT)
    CENTER_FRAME.setStyleSheet("background-color: red")
    MODAL_LAYOUT.addWidget(CENTER_FRAME)
    
    MODAL.show()


def open_imdb():
    webbrowser.open("https://www.imdb.com/title/tt0468569")
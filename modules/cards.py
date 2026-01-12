import PyQt6.QtWidgets as widgets
from PIL import Image
# class for change from pil to qt
from PIL.ImageQt import ImageQt
import requests, random
import PyQt6.QtGui as gui
from utils import api_request, api_req
from io import BytesIO

def cadrs(third_frame, third_frame_layout, row, name_film):
    if name_film == None:
        info = api_request()
        index = random.randint(0, 99)
        response = requests.get(info[index]["image"])
    elif name_film != None:
        info = api_req(name_film= name_film)
        response = requests.get(info["image"])
    image_bytes = BytesIO(response.content)
    poster = Image.open(image_bytes)
    qt_poster = ImageQt(poster)
    label3 = widgets.QLabel(parent= third_frame)
    pixmap2 = gui.QPixmap(gui.QImage(qt_poster))
    pixmap2 = pixmap2.scaled(200, 309)
    label3.setPixmap(pixmap2)
    third_frame_layout.addWidget(label3, 1, row)

def info_btn(third_frame, third_frame_layout, row):
    info_btn = widgets.QPushButton(third_frame)
    info_btn.setStyleSheet("background-color: none; border-radius: 5px")
    info_btn.setFixedSize(200, 309)
    third_frame_layout.addWidget(info_btn, 1, row)
    info_btn.clicked.connect(test)
def test():
    print("aaa")

import os
import PyQt6.QtWidgets as widgets
from PIL import Image
from PIL.ImageQt import ImageQt
import PyQt6.QtGui as gui


class ImageLoad:
    def __init__(self,width, height, frame, frame_layout, img = None, bytes_img = None, row= None, col= None):
        if img != None:
            self.image_logo = Image.open(os.path.abspath(os.path.join(__file__, "..", "..", "images", f"{img}")))
        else:
            self.image_logo = Image.open(bytes_img)
        self.qt_image = ImageQt(self.image_logo)
        self.label = widgets.QLabel(parent= frame)
        self.pixmap = gui.QPixmap(gui.QImage(self.qt_image))
        pixmap = self.pixmap.scaled(width, height)
        self.label.setPixmap(pixmap)
        if row != None and col != None:
            frame_layout.addWidget(self.label, row, col)
        else:
            frame_layout.addWidget(self.label)
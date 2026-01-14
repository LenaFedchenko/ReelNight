import PyQt6.QtWidgets as widgets
from .app import app
from .widgets import Widget
from .frames import Frame
from PIL import Image
# class for change from pil to qt
from PIL.ImageQt import ImageQt
import os
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from .cards import cadrs, info_btn
from utils.api_requests import search_film


class Main_Window(widgets.QMainWindow):
    def __init__(self, name_title, color):
        super().__init__()
        self.window_width = 1200
        self.window_height = 800
        
        self.SCREEN = app.primaryScreen()
        self.screen_size = self.SCREEN.size()
        self.SCREEN_WIDTH = self.screen_size.width()
        self.SCREEN_HEIGHT = self.screen_size.height()

        self.center_x = (self.SCREEN_WIDTH - self.window_width) // 2
        self.center_y = (self.SCREEN_HEIGHT - self.window_height) // 2 

        self.setGeometry(self.center_x, self.center_y, 1200, 800)
        self.setWindowTitle(name_title)
        self.setStyleSheet(f"background-color: {color}")
        
        central_widget = Widget(1200, 800, self)
        main_frame = Frame(parent= central_widget, color= "#111318", width=1200, height= 800)
        first_frame = Frame(parent= main_frame, color= "#111318", width=1200, height= 205)
        second_frame = Frame(parent= main_frame, color= "#111318", width=1200, height= 142)
        self.third_frame = Frame(parent= main_frame, color= "#111318", width=1200, height= 445)

        main_frame_layout = widgets.QVBoxLayout()
        main_frame.setLayout(main_frame_layout)
        first_frame_layout = widgets.QGridLayout()
        first_frame.setLayout(first_frame_layout)
        second_frame_layout = widgets.QGridLayout()
        second_frame.setLayout(second_frame_layout)
        self.third_frame_layout = widgets.QGridLayout()
        self.third_frame.setLayout(self.third_frame_layout)

        main_frame_layout.addWidget(first_frame)
        main_frame_layout.addWidget(second_frame)
        main_frame_layout.addWidget(self.third_frame)


        # load our picture
        image_logo = Image.open(os.path.abspath(os.path.join(__file__, "..", "..", "images", "logo.png")))
        # changed picture for PQt6
        qt_image = ImageQt(image_logo)
        label2 = widgets.QLabel(parent= first_frame)
        pixmap = gui.QPixmap(gui.QImage(qt_image))
        pixmap = pixmap.scaled(400, 109)
        label2.setPixmap(pixmap)
        first_frame_layout.addWidget(label2, 1, 1)

        self.enter_text = widgets.QLineEdit(parent=first_frame)
        self.enter_text.setPlaceholderText("Search")
        self.enter_text.setStyleSheet("background-color: #1E2028; border-radius: 29px; font-size: 20px; padding-left: 20px; color: white")
        self.enter_text.setFixedSize(943, 59)
        
        button_search = widgets.QPushButton(parent= first_frame, text= "Search")
        button_search.setStyleSheet("background-color: #1D1E26; color: #70767C; border-radius: 10px")
        button_search.setFixedSize(core.QSize(108, 36))
        
        button_search.clicked.connect(self.search)

        first_frame_layout.addWidget(self.enter_text, 2, 1)
        first_frame_layout.addWidget(button_search, 2, 2)

        movie = widgets.QLabel(parent= second_frame, text="Movies")
        second_frame_layout.addWidget(movie, 1, 1)
        movie.setStyleSheet("font-size: 36px; color: white")

        button_action = widgets.QPushButton(parent= second_frame, text= "Action")
        button_action.setStyleSheet("background-color: #1D1E26; color: #70767C; border-radius: 10px")
        button_action.setFixedSize(core.QSize(158, 46))

        button_drama = widgets.QPushButton(parent= second_frame, text= "Drama")
        button_drama.setStyleSheet("background-color: #1D1E26; color: #70767C; border-radius: 10px")
        button_drama.setFixedSize(core.QSize(158, 46))

        button_comedy = widgets.QPushButton(parent= second_frame, text= "Comedy")
        button_comedy.setStyleSheet("background-color: #1D1E26; color: #70767C; border-radius: 10px")
        button_comedy.setFixedSize(core.QSize(158, 46))

        button_horror = widgets.QPushButton(parent= second_frame, text= "Horror")
        button_horror.setStyleSheet("background-color: #1D1E26; color: #70767C; border-radius: 10px")
        button_horror.setFixedSize(core.QSize(158, 46))
        
        button_action.clicked.connect(self.click)
        button_drama.clicked.connect(self.click)
        button_comedy.clicked.connect(self.click)
        button_horror.clicked.connect(self.click)

        second_frame_layout.addWidget(button_action, 2, 1)
        second_frame_layout.addWidget(button_drama, 2, 2)
        second_frame_layout.addWidget(button_comedy, 2, 3)
        second_frame_layout.addWidget(button_horror, 2, 4)

        for i in range(5):
            # card = Card()
            cadrs(self.third_frame, self.third_frame_layout, i, name_film= None)
            info_btn(self.third_frame, self.third_frame_layout, i, frame= main_frame)


    def search(self):
        # search = Card()
        film_name = self.enter_text.text()
        search_film(name_film=film_name.lower())
        cadrs(self.third_frame, self.third_frame_layout, 0, name_film= film_name)

    def click(self):
        print("a")
    

main_window = Main_Window(name_title="ReelNight", color="#111318")
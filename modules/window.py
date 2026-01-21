import PyQt6.QtWidgets as widgets
from .app import app
from .widgets import Widget
from .frames import Frame
from PIL import Image
# class for change from pil to qt
from PIL.ImageQt import ImageQt
import os, random
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from .cards import cadrs, info_btn
from utils.api_requests import search_film, filter
from .load_image import ImageLoad


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
        
        main_frame_layout = widgets.QVBoxLayout()
        first_frame_layout = widgets.QGridLayout()
        second_frame_layout = widgets.QGridLayout()
        self.third_frame_layout = widgets.QGridLayout()

        central_widget = Widget(1200, 800, self)
        self.main_frame = Frame(parent= central_widget, color= "#111318", width=1200, height= 800, layout=main_frame_layout)
        first_frame = Frame(parent= self.main_frame, color= "#111318", width=1200, height= 205, layout= first_frame_layout)
        second_frame = Frame(parent= self.main_frame, color= "#111318", width=1200, height= 142, layout= second_frame_layout)
        self.third_frame = Frame(parent= self.main_frame, color= "#111318", width=1200, height= 445, layout= self.third_frame_layout)


        main_frame_layout.addWidget(first_frame)
        main_frame_layout.addWidget(second_frame)
        main_frame_layout.addWidget(self.third_frame)

        image_logo = ImageLoad(width=400, height=109, img="logo.png", frame= first_frame, frame_layout= first_frame_layout, row=1, col=1)

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

        genres = ["Fantasy", "Drama", "Comedy", "Horror", "Sci-Fi", "Animation", "Family", "Adventure","Mystery", "Thriller", "Film-Noir", "War", "Crime"]
        for j in range(1, 5):
            random_genres = random.randint(0, 12)

            self.btn = widgets.QPushButton(parent= second_frame, text= f"{genres[random_genres]}")
            self.btn.setStyleSheet("background-color: #1D1E26; color: #70767C; border-radius: 10px")
            self.btn.setFixedSize(core.QSize(158, 46))
            self.btn.clicked.connect(self.click)
            second_frame_layout.addWidget(self.btn, 2, j)
            
        for i in range(5):
            index = cadrs(self.third_frame, self.third_frame_layout, i, name_film= None)
            info_btn(self.third_frame, self.third_frame_layout, i, frame= self.main_frame, index_poster= index)


    def search(self):
        film_name = self.enter_text.text()
        search_film(name_film=film_name.lower())
        index2 = cadrs(self.third_frame, self.third_frame_layout, 0, name_film= film_name)
        info_btn(self.third_frame, self.third_frame_layout, 0, frame= self.main_frame, index_poster= index2)

    def click(self):
        btn = self.sender()
        genre_pressed = btn.text()
        filter_genre = filter(genre_pressed)
        i = 1
        for genre_film in filter_genre:
            if i < 5:
                i += 1
                index = cadrs(self.third_frame, self.third_frame_layout, i, name_film= None, genre= genre_film)
                info_btn(self.third_frame, self.third_frame_layout, i, frame= self.main_frame, index_poster= index)
    

main_window = Main_Window(name_title="ReelNight", color="#111318")
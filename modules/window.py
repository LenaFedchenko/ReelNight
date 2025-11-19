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
        first_frame = Frame(parent= main_frame, color= "#184CCF", width=1200, height= 205)
        second_frame = Frame(parent= main_frame, color= "#3DCF18", width=1200, height= 142)
        third_frame = Frame(parent= main_frame, color= "#CF1818", width=1200, height= 445)

        main_frame_layout = widgets.QVBoxLayout()
        main_frame.setLayout(main_frame_layout)
        first_frame_layout = widgets.QGridLayout()
        first_frame.setLayout(first_frame_layout)

        main_frame_layout.addWidget(first_frame)
        main_frame_layout.addWidget(second_frame)
        main_frame_layout.addWidget(third_frame)

        # load our picture
        image_logo = Image.open(os.path.abspath(os.path.join(__file__, "..", "..", "images", "logo.png")))
        # changed picture for PQt6
        qt_image = ImageQt(image_logo)
        label2 = widgets.QLabel(parent= first_frame)
        pixmap = gui.QPixmap(gui.QImage(qt_image))
        pixmap = pixmap.scaled(400, 109)
        label2.setPixmap(pixmap)
        first_frame_layout.addWidget(label2, 1, 1)


        enter_text = widgets.QLineEdit(parent= first_frame)
        enter_text.setPlaceholderText("enter text")
        

        def func():
            print(enter_text.text())

        enter_text.textChanged.connect(func)
        enter_text.setStyleSheet("background-color: #1E2028; border-radius: 29px; font-size: 20px")
        enter_text.setFixedSize(943, 59)
        

        first_frame_layout.addWidget(enter_text, 2, 1)


    #     # created label
    #     label1 = widgets.QLabel(parent= first_frame, text="hello world")
    #     main_frame_layout.addWidget(label1)
    #     label1.setStyleSheet("font-size: 100px; color: pink;  font-weight:900")



    #     button = widgets.QPushButton(parent= main_frame, text= "push")
    #     button.setStyleSheet("background-color: pink; font-weight: 900;")


    #     def click():
    #         print("aaaaa")


    #     button.clicked.connect(click)

    #     enter_text = widgets.QLineEdit(parent=main_frame)
    #     enter_text.setPlaceholderText("enter text")

    #     def func():
    #         print(enter_text.text())

    #     enter_text.textChanged.connect(func)


    #     down_list = widgets.QComboBox(parent= main_frame)
    #     down_list.addItem("Afrika")
    #     down_list.addItem("Amerika")
    #     down_list.addItem(gui.QIcon("images/monkey.png"), "hello")
    #     down_list.currentTextChanged.connect(func)

    #     main_frame_layout.addWidget(button, 3, 2)
    #     main_frame_layout.addWidget(enter_text, 4, 4)


    # def mousePressEvent(self, event: gui.QMouseEvent):
    #     if event.button() == core.Qt.MouseButton.LeftButton:
    #         print("click")

    # def mouseMoveEvent(self, event: gui.QMouseEvent):
    #     position = event.position()
    #     point_pos = position.toPoint()
    #     print(point_pos)

    # def mouseReleaseEvent(self, event: gui.QMouseEvent):
    #     event.button()

main_window = Main_Window(name_title="ReelNight", color="#111318")
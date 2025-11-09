import PyQt6.QtWidgets as widgets
from .app import app
from PIL import Image
# class for change from pil to qt
from PIL.ImageQt import ImageQt
import PyQt6.QtGui as gui

main_window = widgets.QMainWindow()

window_width = 1200
window_height = 800

screen = app.primaryScreen()
screen_size = screen.size()
SCREEN_WIDTH = screen_size.width()
SCREEN_HEIGHT = screen_size.height()

center_x = (SCREEN_WIDTH - window_width) // 2
center_y = (SCREEN_HEIGHT - window_height) // 2 

main_window.setGeometry(center_x, center_y, 1200, 800)
main_window.setWindowTitle("ReelNight")
main_window.setStyleSheet("background-color: #111318")

central_widget = widgets.QWidget(parent=main_window)
central_widget.setFixedWidth(1200)
central_widget.setFixedHeight(800)

main_frame = widgets.QFrame(parent= central_widget)
first_frame = widgets.QFrame(parent= main_frame)
second_frame = widgets.QFrame(parent= main_frame)
main_frame.setStyleSheet("background-color: #111318")
second_frame.setStyleSheet("background-color: green")
first_frame.setStyleSheet("background-color: white")
main_frame.setFixedWidth(1200)
main_frame.setFixedHeight(800)
second_frame.setFixedWidth(100)
second_frame.setFixedHeight(100)
first_frame.setFixedWidth(100)
first_frame.setFixedHeight(100)

# сетка размещения
main_frame_layout = widgets.QGridLayout()
main_frame.setLayout(main_frame_layout)
main_frame_layout.addWidget(first_frame, 1, 5)
main_frame_layout.addWidget(second_frame, 1, 1)

# created label
label1 = widgets.QLabel(parent= first_frame, text="hello world")
main_frame_layout.addWidget(label1)
label1.setStyleSheet("font-size: 100px; color: pink;  font-weight:900")

# load our picture
image = Image.open("images/monkey.png")

# changed picture for PQt6
qt_image = ImageQt(image)
label2 = widgets.QLabel(parent= second_frame)


button = widgets.QPushButton(parent= main_frame, text= "push")
button.setStyleSheet("background-color: pink; font-weight: 900;")


def click():
    print("aaaaa")


button.clicked.connect(click)

enter_text = widgets.QLineEdit(parent=main_frame)
enter_text.setPlaceholderText("enter text")

def func():
    print(enter_text.text())

enter_text.textChanged.connect(func)


down_list = widgets.QComboBox(parent= main_frame)
down_list.addItem("Afrika")
down_list.addItem("Amerika")
down_list.addItem(gui.QIcon("images/monkey.png"), "hello")
down_list.currentTextChanged.connect(func)

main_frame_layout.addWidget(button, 3, 2)
main_frame_layout.addWidget(enter_text, 4, 4)
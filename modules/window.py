import PyQt6.QtWidgets as widgets
from .app import app

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

import PyQt6.QtWidgets as widgets

app = widgets.QApplication([])
main_window = widgets.QMainWindow()

main_window.setGeometry(150, 150, 1200, 800)

main_window.show()
app.exec()
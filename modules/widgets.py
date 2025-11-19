import PyQt6.QtWidgets as widgets

class Widget(widgets.QWidget):
    def __init__(self, width, height, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        
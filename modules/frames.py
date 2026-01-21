import PyQt6.QtWidgets as widgets

class Frame(widgets.QFrame):
    def __init__(self, parent, width, height, layout, color = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setStyleSheet(f"background-color: {color}")
        self.setFixedSize(width, height)
        self.setLayout(layout)
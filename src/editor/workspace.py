from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout

class Workspace(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Workspace")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

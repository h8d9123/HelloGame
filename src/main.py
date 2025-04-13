from PySide6.QtWidgets import QApplication
from editor.editor_window import EditorWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorWindow()
    window.show()
    sys.exit(app.exec())
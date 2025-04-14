from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMdiArea, QTabWidget
from game_loop import GameLoop
import threading
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from pathlib import Path
from PySide6.QtGui import QAction, QIcon
import editor.resource.res_qrc
g_tool_bar_actions = {
    "new_project": {"icon":":/pic/icon/new_project.png", "status_tip":"Create a new project"},
    "open_project": {"icon":":/pic/icon/open_project.png", "status_tip":"Open a project"},
    "save_project": {"icon":":/pic/icon/save_project.png", "status_tip":"Save the project"},
}
class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 加载UI文件
        current_dir = Path(__file__).parent
        ui_file = QFile(current_dir / "ui" / "editor_window.ui")
        ui_file.open(QFile.ReadOnly)
        
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        self.setCentralWidget(self.ui)
        self.setWindowTitle("HelloGame")
        self.setGeometry(100, 100, 800, 600)
        self.init_toolbar()
        self.init_mdi()
        self.game_thread = None

    def start_game(self):
        if self.game_thread is None or not self.game_thread.is_alive():
            self.game_thread = threading.Thread(target=GameLoop().run, daemon=True)
            self.game_thread.start()
    def init_toolbar(self):
        for action in g_tool_bar_actions:
            button_action = QAction(self)
            button_action.setIcon(QIcon(g_tool_bar_actions[action]["icon"]))
            button_action.setStatusTip(g_tool_bar_actions[action]["status_tip"])
            #button_action1.triggered.connect(self.toolbar_button_clicked)
            self.ui.toolBar.addAction(button_action)
    def init_mdi(self):
        self.mdi_area = QMdiArea()
        self.ui.centralwidget.layout().addWidget(self.mdi_area, stretch=4)
        self.bottom_area = QTabWidget()
        self.ui.centralwidget.layout().addWidget(self.bottom_area, stretch=1)


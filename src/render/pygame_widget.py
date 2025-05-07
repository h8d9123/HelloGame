import sys
from PySide6.QtGui import QPaintEvent
import pygame
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDialog, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QImage

class PygameWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_OpaquePaintEvent)
        #self.setAttribute(Qt.WA_PaintOnScreen) // WA_PaintOnScreen是直接在屏幕上绘制，不使用双缓冲,不会触发paintevent事件
        self.setFocusPolicy(Qt.StrongFocus)
        pygame.init()
        self.surface = pygame.Surface((640, 480))  # 只使用 Surface，不创建 SDL 窗口
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  # 定时刷新界面
        self.timer.start(16)  # 60 FPS

    def resizeEvent(self, event):
        size = event.size()
        self.surface = pygame.Surface((size.width(), size.height()))  # 动态调整 Surface 尺寸

    def paintEvent(self, event: QPaintEvent) -> None:
        # 用 Pygame 在 surface 上绘图
        self.surface.fill((0, 0, 0))
        w = self.surface.get_width()
        h = self.surface.get_height()
        pygame.draw.circle(self.surface, (255, 0, 0), (self.surface.get_width() // 2, self.surface.get_height() // 2), 50, width=3)
        # 转换为 QImage
        data = pygame.image.tostring(self.surface, 'RGB')
        image = QImage(data, self.surface.get_width(), self.surface.get_height(), QImage.Format_RGB888)

        # 绘制到 Qt 控件中
        painter = QPainter(self)
        painter.drawImage(0,0, image)  # 直接绘制
        painter.end()

    def paintEngine(self):
        return None  # 禁用 Qt 默认的绘图引擎
    
class GameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Run Game")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        #layout.addWidget(QLabel("123"))

        # 创建并添加 PygameWidget
        self.pygame_widget = PygameWidget(self)
        layout.addWidget(self.pygame_widget)

        self.setLayout(layout)

        # 强制调用一次 update，确保绘制开始
        self.pygame_widget.update()

from PySide6.QtWidgets import QPlainTextEdit, QWidget
from PySide6.QtCore import Qt
from collections import deque
from PySide6.QtWidgets import QVBoxLayout

class BreakPointWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.log_text = QPlainTextEdit()
        font = self.log_text.font()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.log_text.setFont(font)
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.log_text)
        self.setLayout(v_layout)
        self.append("todo")

    def append(self, text):
        # 检查滚动条位置
        scrollbar = self.log_text.verticalScrollBar()
        at_bottom = scrollbar.value() == scrollbar.maximum()
        
        # 直接添加文本
        self.log_text.appendPlainText(text)
        
        # 如果之前在底部，则保持在底部
        if at_bottom:
            scrollbar.setValue(scrollbar.maximum())

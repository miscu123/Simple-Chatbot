"""
Board .py file where the bot will be implemented
"""
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import Qt


class Board(QWidget):
    def __init__(self):
        super().__init__()
        # labels and buttons
        self.setFixedSize(600, 600)
        self.setWindowTitle("Funny Chatbot")
        self.label = QLabel("How can I amuse you today?")
        self.input = QLineEdit()
        self.ok = QPushButton("OK")
        self.cancel = QPushButton("Cancel")

        # buttons layout style (H)
        buttons = QHBoxLayout()
        buttons.addWidget(self.ok)
        buttons.addWidget(self.cancel)

        # whole board layout style (V)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        # response area style (V)
        self.response_area = QVBoxLayout()
        self.layout.addLayout(self.response_area)

        self.layout.addStretch(1)

        self.layout.addWidget(self.input)
        self.layout.addLayout(buttons)

        self.setLayout(self.layout)

        self.ok.clicked.connect(self.update_text)
        self.cancel.clicked.connect(self.close)

    def update_text(self):
        text = self.input.text()
        if text.strip():
            response_label = QLabel(f"You: {text}")
            self.response_area.addWidget(response_label)
            self.input.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.update_text()
        elif event.key() == Qt.Key_Escape:
            self.close()
        else:
            event.ignore()
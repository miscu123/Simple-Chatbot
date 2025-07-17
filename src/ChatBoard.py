"""
Board .py file where the bot will be implemented
"""
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import Qt
from Parser import Parser
import json


class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.data = None
        initjson(self)
        self.parser = Parser()

        # labels and buttons
        self.setFixedSize(800, 800)
        self.setWindowTitle("Funny Chatbot")
        self.label = QLabel("Bot: How can I amuse you today?")
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

            # we check if the bot can respond to the question or not
            parsed_text = self.parser.parse_txt(text)
            response = self.data.get(parsed_text)
            if response:
                bot_label = QLabel(f"Bot: {response}")
            else:
                bot_label = QLabel("Bot: Îmi pare rău, nu știu răspunsul la această întrebare.")

            self.response_area.addWidget(bot_label)
            self.input.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.update_text()
        elif event.key() == Qt.Key_Escape:
            self.close()
        else:
            event.ignore()


# json initialization function
def initjson(self):
    with open('./docs/Q&A.json', 'r', encoding='utf-8') as file:
        self.data = json.load(file)
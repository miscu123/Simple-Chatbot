"""
Board .py file where the bot will be implemented
"""
from PySide6 import QtCore
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QScrollArea,
                               QSizePolicy)
from PySide6.QtCore import Qt

from Design import Design
from Options import OptionsDialog
from Parser import Parser
import json


class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.data = None

        # initialize data from Q&A json
        initjson(self)

        # create parser to format the input
        self.parser = Parser()

        # labels and buttons
        self.showFullScreen()
        self.setMinimumSize(600, 600)
        self.setWindowTitle("Funny Chatbot")
        self.label = QLabel("Bot: Cum te pot face să zâmbești?")
        self.label.setObjectName("greetingLabel")
        self.input = QLineEdit()
        self.input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.ok = QPushButton("OK")
        self.cancel = QPushButton("Cancel")
        self.cancel.setObjectName("cancel")  # IMPORTANT: setează ID-ul pentru CSS
        self.options = QPushButton("Options")

        # buttons layout style (H)
        buttons = QHBoxLayout()
        buttons.addWidget(self.ok)
        buttons.addWidget(self.cancel)
        buttons.addWidget(self.options)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.messages_widget = QWidget()
        self.messages_layout = QVBoxLayout()
        self.messages_layout.setAlignment(Qt.AlignTop)
        self.messages_widget.setLayout(self.messages_layout)

        self.scroll_area.setWidget(self.messages_widget)

        # whole board layout style (V)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.input)
        self.layout.addLayout(buttons)

        self.setLayout(self.layout)
        self.button_pressed()

        self.design = Design(self)

    # function for when we press a button
    def button_pressed(self):
        self.ok.clicked.connect(self.update_text)
        self.cancel.clicked.connect(self.close)
        self.options.clicked.connect(self.show_commands)

    def update_text(self):
        # Get input
        text = self.input.text().strip()
        if not text:
            return  # Skip if empty

        user_msg = QLabel(f"You: {text}")
        self.design.style_message_label(user_msg, 'user')

        # user message
        user_container = QWidget()
        user_layout = QHBoxLayout()
        user_layout.addStretch(1)
        user_layout.addWidget(user_msg)
        user_container.setLayout(user_layout)
        self.messages_layout.addWidget(user_container)

        # bot response
        matched_key = self.parser.match_fuzzy(text, self.data.keys())
        bot_response = self.data[
            matched_key] if matched_key else "Îmi pare rău, nu știu răspunsul la această întrebare."

        # bot message
        bot_msg = QLabel(f"Bot: {bot_response}")
        self.design.style_message_label(bot_msg, 'bot')

        # Setup bot message container
        bot_container = QWidget()
        bot_layout = QHBoxLayout()
        bot_layout.addWidget(bot_msg)
        bot_layout.addStretch(1)  # Push left
        bot_container.setLayout(bot_layout)
        self.messages_layout.addWidget(bot_container)

        self.input.clear()

        # Force UI update
        self.messages_widget.updateGeometry()
        self.messages_layout.update()

        # Auto-scroll with delay
        QtCore.QTimer.singleShot(50, lambda: self.scroll_to_bottom())

    def scroll_to_bottom(self):
        scroll_bar = self.scroll_area.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())
        QtCore.QTimer.singleShot(10, lambda: scroll_bar.setValue(scroll_bar.maximum()))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.update_text()
        elif event.key() == Qt.Key_Escape:
            self.close()
        else:
            event.ignore()

    def show_commands(self):
        if not self.data:
            return

        dialog = OptionsDialog(commands=self.data.keys(), parent=self)
        dialog.exec()


# json initialization function
def initjson(self):
    with open('./docs/Q&A.json', 'r', encoding='utf-8') as file:
        self.data = json.load(file)
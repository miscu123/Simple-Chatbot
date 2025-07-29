from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QListWidget, QHBoxLayout
from PySide6.QtGui import QFont


class OptionsDialog(QDialog):
    def __init__(self, commands, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chatbot commands")
        self.setMinimumSize(400, 300)

        # option dialog layout (V)
        layout = QVBoxLayout()

        label = QLabel("Available commands:")
        label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(label)

        # show the available commands
        self.list_widget = QListWidget()
        self.list_widget.addItems(sorted(commands))
        layout.addWidget(self.list_widget)

        # close button layout (H)
        button_layout = QHBoxLayout()
        close_btn = QPushButton("Close window")
        close_btn.clicked.connect(self.close)
        button_layout.addStretch()
        button_layout.addWidget(close_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)
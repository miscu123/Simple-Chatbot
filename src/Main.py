"""
The main .py file where the board will be called
"""
import sys
from PySide6.QtWidgets import QApplication
from ChatBoard import Board

app = QApplication(sys.argv)
window = Board()
window.show()
sys.exit(app.exec())
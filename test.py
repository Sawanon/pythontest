import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout

class Myapp(QWidget):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

window = Myapp()
window.show()

app.exec()
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Admin_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('키오스크 관리자')
        self.setFixedSize(480,830)
        
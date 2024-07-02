import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def makezoom(text):
    btn = QPushButton()
    btn.setFixedSize(60, 60)
    btn.setStyleSheet(
        u"border: 1px solid rgba(0,0,0,0); border-radius: 16px; Background-color: rgb(255,126,0);font-weight:Bold; color: white; font-size: 90px;")
    btn.setText(text)
    return btn

def btnSetNHome(w, h, img):
    # 세팅버튼 및 홈버튼 정의
    btn = QPushButton()
    btn.setStyleSheet(
        f"QPushButton {{ background-image: url('{img}');"
        f"background-position: center;"
        f"background-repeat: no-repeat;"
        f"background-size: cover;}}")
    btn.setFixedSize(w, h)
    btn.setFlat(1)
    return btn

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작
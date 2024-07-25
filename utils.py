from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont

fontTitle = QFont("SUITE Bold", 35)
fontMiddle = QFont("SUITE", 25)
fontSmall = QFont("SUITE", 16)
fontCount = 0

def makeBtn(w, h, text, parents):
    # 버튼 생성하는 함수
    btn = QPushButton()
    btn.setFixedSize(w, h)
    btn.setText(text)
    btn.setParent(parents)
    return btn

def makeLabel(w, h, text, parents):
    # 라벨 생성하는 함수
    label = QLabel()
    label.setFixedSize(w, h)
    label.setText(text)
    label.setParent(parents)
    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    return label

def updateFontSize():
    global fontTitle, fontMiddle, fontSmall
    return fontTitle, fontMiddle, fontSmall

def setFontCount(count):
    global fontCount
    fontCount = count

def getFontCount():
    global fontCount
    return fontCount

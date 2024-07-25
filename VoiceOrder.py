# VoiceOrder.py
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils import makeBtn, makeLabel, updateFontSize, setFontCount, getFontCount
import speech_recognition as sr
import pyttsx3

class VoiceOrder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("음성 주문")
        self.setFixedSize(480, 830)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupVoiceUI()

    def setupVoiceUI(self):
        self.PageVoiceMain = QWidget()
        self.setCentralWidget(self.PageVoiceMain)
        self.PageVoiceMain.setStyleSheet("background-color: rgb(255,255,255);")

        def makezoom(text):
            btn = QPushButton()
            btn.setFixedSize(50, 50)
            btn.setStyleSheet(
                u"border: 1px solid rgba(0,0,0,0); border-radius: 10px; Background-color: rgb(255,126,0);font-weight:Bold; color: white; font-size: 40px;")
            btn.setText(text)
            btn.setParent(self.PageVoiceMain)
            return btn

        LabelZoom = makeLabel(105, 30, "글씨 크기", self.PageVoiceMain)
        LabelZoom.setGeometry(365, 35, 105, 30)

        BtnZoomIn = makezoom("+")
        BtnZoomOut = makezoom("-")
        BtnZoomIn.setGeometry(365, 70, 50, 50)
        BtnZoomOut.setGeometry(420, 70, 50, 50)
        BtnZoomIn.clicked.connect(self.increasefont)
        BtnZoomOut.clicked.connect(self.decreasefont)

        self.LabelInfo = makeLabel(440, 100, "주문 시작 버튼을 누르고\n 메뉴 이름을 말씀해주세요.", self.PageVoiceMain)
        self.LabelInfo.setGeometry(20, 200, 440, 100)

        self.BtnBack = makeBtn(50, 50, "홈", self.PageVoiceMain)
        self.BtnBack.setGeometry(10, 40, 50, 50)
        self.BtnBack.clicked.connect(self.close)

        self.BtnActivate = makeBtn(120, 120, "시작", self.PageVoiceMain)
        self.BtnActivate.setGeometry(180, 430, 120, 120)

        fontTitle, fontMiddle, _ = updateFontSize()
        self.LabelInfo.setFont(fontMiddle)

    def updateFont(self):
        fontTitle, fontMiddle, fontSmall = updateFontSize()
        self.LabelInfo.setFont(fontMiddle)

    def increasefont(self):
        fontCount = getFontCount()
        if fontCount < 5:
            setFontCount(fontCount + 1)
            fontTitle, fontMiddle, fontSmall = updateFontSize()
            fontTitle.setPointSize(fontTitle.pointSize() + 1)
            fontMiddle.setPointSize(fontMiddle.pointSize() + 1)
            fontSmall.setPointSize(fontSmall.pointSize() + 1)
            self.updateFont()

    def decreasefont(self):
        fontCount = getFontCount()
        if fontCount > -5:
            setFontCount(fontCount - 1)
            fontTitle, fontMiddle, fontSmall = updateFontSize()
            fontTitle.setPointSize(fontTitle.pointSize() - 1)
            fontMiddle.setPointSize(fontMiddle.pointSize() - 1)
            fontSmall.setPointSize(fontSmall.pointSize() - 1)
            self.updateFont()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VoiceOrder()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작

# VoiceOrder.py
import sys
import time

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

        self.BtnActivate = makeBtn(120, 120, "", self.PageVoiceMain)
        self.BtnActivate.setGeometry(180, 430, 120, 120)
        self.BtnActivate.setFlat(1)
        self.BtnActivate.clicked.connect(self.voiceActivate)

        self.LabelAct = makeLabel(250,80,"버튼을 누르면\n시작합니다.",self.PageVoiceMain)
        self.LabelAct.setGeometry(115,550,250,80)
        self.img_token = 0
        self.voiceImgChange()
        fontTitle, fontMiddle, _ = updateFontSize()
        self.LabelInfo.setFont(fontMiddle)

    def voiceActivate(self):
        self.listening = False
        if not self.listening:
            self.listening = True
            self.LabelAct.setText("1초 후에\n주문을 시작합니다.")
            self.repaint()
            time.sleep(1)
            self.img_token = 1
            self.voiceImgChange()
            mic = sr.Recognizer()
            with sr.Microphone() as source:
                print("음성 입력 시작")
                self.LabelAct.setText("메뉴 이름을\n말씀하세요")
                self.repaint()
                audio_data = mic.listen(source)
                try:
                    user_input = mic.recognize_google(audio_data,language="ko-KR")
                    print(user_input)
                except sr.UnknownValueError:
                    print("음성 인식 실패")
            self.listening = False
            self.img_token = 0
            self.voiceImgChange()


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

    def voiceImgChange(self):
        if self.img_token == 1 :
            self.LabelAct.setText("지금 말씀하세요!")
            self.BtnActivate.setStyleSheet(
                "QPushButton { background-image: url('img/ClientUI/Voice_On.png');"
                "background-position: center;"
                "background-repeat: no-repeat;"
                "background-size: cover; }"
            )

        elif self.img_token == 0 :
            self.LabelAct.setText("주문 시작")
            self.BtnActivate.setStyleSheet(
                "QPushButton { background-image: url('img/ClientUI/Voice_Off.png');"
                "background-position: center;"
                "background-repeat: no-repeat;"
                "background-size: cover; }"
            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VoiceOrder()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작

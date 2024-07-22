import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def makeBtn(w, h, text, parents):
    # 버튼 생성하는 함수
    btn = QPushButton()
    btn.setFixedSize(w, h)
    btn.setText(text)
    btn.setParent(parents)
    return btn

def makeLabel(w, h, text, parents):
    label = QLabel()
    label.setFixedSize(w, h)
    label.setText(text)
    label.setParent(parents)
    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    return label

fontTitle = QFont("SUITE Bold", 35)
fontMiddle = QFont("SUITE",25)
fontSmall = QFont("SUITE",16)
fontCount = 0

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
            # 텍스트 크기 조절하는 버튼 생성
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


    def updateFont(self):
        print("업데이트 테스트")

    def increasefont(self):
        global fontCount
        if fontCount < 5 :
            fontCount += 1
            fontTitle.setPointSize(fontTitle.pointSize()+1)
            fontMiddle.setPointSize(fontMiddle.pointSize()+1)
            fontSmall.setPointSize(fontSmall.pointSize()+1)
            self.updateFont()

    def decreasefont(self):
        global fontCount
        if fontCount > -5 :
            fontCount -= 1
            fontTitle.setPointSize(fontTitle.pointSize()-1)
            fontMiddle.setPointSize(fontMiddle.pointSize()-1)
            fontSmall.setPointSize(fontSmall.pointSize()-1)
            self.updateFont()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VoiceOrder()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작

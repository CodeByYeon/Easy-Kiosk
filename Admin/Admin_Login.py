import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from utils import makeBtn, makeLabel, fontTitle, fontSmall, fontMiddle

class Admin_Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('키오스크 관리자')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(480, 830)
        self.currentPW = ""
        self.setupUI()

    def setupUI(self):
        self.MainWidget = QWidget(self)
        self.MainWidget.setStyleSheet("Background-color: rgb(255, 255, 255);")
        self.MainWidget.setFixedSize(480, 830)
        self.setCentralWidget(self.MainWidget)

        # 라벨을 담기 위한 프레임 생성
        FramePW = QFrame(self.MainWidget)
        FramePW.setGeometry(40, 40, 400, 180)
        self.LayoutPW = QVBoxLayout(FramePW)
        self.LayoutPW.setSpacing(10)

        # 라벨 생성
        self.LabelAdmin = makeLabel(400, 70, "관리자 인증", self.MainWidget)
        self.LabelAdmin.setFont(fontTitle)
        self.LayoutPW.addWidget(self.LabelAdmin, alignment=Qt.AlignCenter)

        # 비밀번호 틀렸을 때 안내 생성
        self.LabelWrongPW = makeLabel(400, 20, "잘못된 비밀번호입니다. 초기 비밀번호:1234", self.MainWidget)
        self.LabelWrongPW.setFont(fontSmall)
        self.LabelWrongPW.setStyleSheet("color: red;")
        self.LabelWrongPW.setHidden(True)
        self.LayoutPW.addWidget(self.LabelWrongPW, alignment=Qt.AlignCenter)

        self.LayoutPWForm = QHBoxLayout()
        self.PWLabels = [makeLabel(40, 70, "○", self.MainWidget) for _ in range(4)]
        for label in self.PWLabels:
            label.setFont(fontTitle)
            label.setAlignment(Qt.AlignCenter)
            self.LayoutPWForm.addWidget(label)

        self.LayoutPW.addLayout(self.LayoutPWForm)
        self.setupGridLayout()

        self.LabelQuit = makeBtn(40, 30, "✕", self.MainWidget)
        self.LabelQuit.setFont(fontSmall)
        self.LabelQuit.setFlat(True)
        self.LabelQuit.clicked.connect(self.close)
        self.LabelQuit.setGeometry(10, 40, 30, 30)

    def setupGridLayout(self):
        FrameGrid = QFrame(self.MainWidget)
        FrameGrid.setGeometry(40, 280, 400, 520)
        self.GridPW = QGridLayout(FrameGrid)
        self.GridPW.setSpacing(10)
        self.GridPW.setContentsMargins(5, 5, 5, 5)

        self.BtnSubmit = QPushButton(FrameGrid)
        self.BtnSubmit.setFont(fontMiddle)
        self.BtnSubmit.setText("입력")
        self.BtnSubmit.setStyleSheet("background-color:rgb(255, 255, 255);border: 2px solid rgb(0, 0, 0);")
        self.BtnSubmit.clicked.connect(self.checkPassword)

        self.BtnDel = QPushButton(FrameGrid)
        self.BtnDel.setFont(fontMiddle)
        self.BtnDel.setText("삭제")
        self.BtnDel.setStyleSheet("background-color:rgb(255,255,255);border: 2px solid rgb(255, 0, 0);color: red;")
        self.BtnDel.clicked.connect(self.clearPassword)
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.BtnDel.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.BtnSubmit.sizePolicy().hasHeightForWidth())
        self.BtnDel.setSizePolicy(sizePolicy)
        self.BtnSubmit.setSizePolicy(sizePolicy)

        button_texts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.buttons = []
        for text in button_texts:
            button = QPushButton(text)
            self.buttons.append(button)
        for i, button in enumerate(self.buttons):
            setattr(self, f"Num{i}", button)
            button.setFont(fontSmall)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            button.setStyleSheet("background-color:rgb(255,255,255);border: 2px solid rgb(0, 0, 0);")
            button.setFlat(True)
        positions = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2), (3, 0)]
        for i, button in enumerate(self.buttons):
            button.clicked.connect(lambda _, digit=i: self.addDigit(str(digit)))
        for widget, (row, col) in zip(self.buttons + [self.BtnSubmit, self.BtnDel], positions):
            self.GridPW.addWidget(widget, row, col, 1, 1)

    def addDigit(self, digit):
        if len(self.currentPW) < 4:
            self.currentPW += digit
            self.updatePWDisplay()

    def updatePWDisplay(self):
        for i in range(4):
            self.PWLabels[i].setText("●" if i < len(self.currentPW) else "○")

    def clearPassword(self):
        self.currentPW = ""
        self.updatePWDisplay()

    def checkPassword(self):
        if self.currentPW == "1234":  # 초기 비밀번호 확인
            from Admin_Main import Admin_Main
            print("비밀번호가 올바릅니다.")
            self.LabelWrongPW.setHidden(True)
            main = Admin_Main()
            main.show()
        else:
            self.LabelWrongPW.setHidden(False)
        self.clearPassword()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Admin_Login()
    window.show()
    sys.exit(app.exec_())

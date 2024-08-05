import sys
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
        self.setCentralWidget(self.MainWidget)

        FramePW = QFrame(self.MainWidget)
        FramePW.setGeometry(40, 40, 400, 180)
        LayoutPW = QVBoxLayout(FramePW)
        LayoutPW.setSpacing(10)

        self.LabelAdmin = makeLabel(400, 70, "관리자 인증", self.MainWidget)
        self.LabelAdmin.setFont(fontTitle)
        LayoutPW.addWidget(self.LabelAdmin, alignment=Qt.AlignCenter)

        self.LabelWrongPW = makeLabel(400, 20, "잘못된 비밀번호입니다. 초기 비밀번호:1234", self.MainWidget)
        self.LabelWrongPW.setFont(fontSmall)
        self.LabelWrongPW.setStyleSheet("color: red;")
        self.LabelWrongPW.setHidden(True)
        LayoutPW.addWidget(self.LabelWrongPW, alignment=Qt.AlignCenter)

        LayoutPWForm = QHBoxLayout()
        self.PWLabels = [makeLabel(40, 70, "○", self.MainWidget) for _ in range(4)]
        for label in self.PWLabels:
            label.setFont(fontTitle)
            label.setAlignment(Qt.AlignCenter)
            LayoutPWForm.addWidget(label)

        LayoutPW.addLayout(LayoutPWForm)

        self.LabelQuit = makeBtn(40, 40, "✕", self.MainWidget)
        self.LabelQuit.setFont(fontSmall)
        self.LabelQuit.setFlat(True)
        self.LabelQuit.clicked.connect(self.close)
        self.LabelQuit.setGeometry(10, 40, 40, 40)

        self.setupGridLayout()

    def setupGridLayout(self):
        FrameGrid = QFrame(self.MainWidget)
        FrameGrid.setGeometry(40, 280, 400, 520)
        GridPW = QGridLayout(FrameGrid)
        GridPW.setSpacing(10)
        GridPW.setContentsMargins(5, 5, 5, 5)

        self.BtnSubmit = self.createButton("입력", self.checkPassword)
        self.BtnDel = self.createButton("삭제", self.clearPassword, "rgb(255, 0, 0)", "red")

        button_texts = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        positions = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 2), (3, 0)]

        self.buttons = [self.createButton(text, lambda _, digit=text: self.addDigit(digit)) for text in button_texts]

        for widget, (row, col) in zip(self.buttons + [self.BtnSubmit, self.BtnDel], positions):
            GridPW.addWidget(widget, row, col, 1, 1)

    def createButton(self, text, callback, border_color="rgb(0, 0, 0)", text_color="black"):
        button = QPushButton(text)
        button.setFont(fontMiddle)
        button.setStyleSheet(f"background-color:rgb(255,255,255);border: 2px solid {border_color};color: {text_color};")
        button.clicked.connect(callback)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy)
        return button

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

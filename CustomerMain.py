import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils import makeBtn, makeLabel, updateFontSize, setCount, getCount

class CustomerMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(u"Background-color:rgb(255, 255, 255);")
        self.setFixedSize(480, 830)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.order_method = ""  # 주문 방법을 저장할 변수
        self.setWindowTitle("Easy-Kiosk v1.0")
        self.makeStackUI()

    def makeStackUI(self):
        # UI를 스택위젯형태로 생성
        self.WidgetMain = QWidget(self)
        self.setCentralWidget(self.WidgetMain)
        self.WidgetMain.setFixedSize(480, 830)

        self.LabelWelcomeMain = makeLabel(350, 85, "선택해주세요", self.WidgetMain)
        self.LabelWelcomeMain.setGeometry(10, 35, 350, 85)

        def makezoom(text):
            btn = QPushButton()
            btn.setFixedSize(50, 50)
            btn.setStyleSheet(
                u"border: 1px solid rgba(0,0,0,0); border-radius: 10px; Background-color: rgb(255,126,0);font-weight:Bold; color: white; font-size: 40px;")
            btn.setText(text)
            btn.setParent(self.WidgetMain)
            return btn

        LabelZoom = makeLabel(105, 30, "글씨 크기", self.WidgetMain)
        LabelZoom.setGeometry(365, 35, 105, 30)

        # 확대, 축소 버튼 만들기
        BtnZoomIn = makezoom("+")
        BtnZoomOut = makezoom("-")
        BtnZoomIn.setGeometry(365, 70, 50, 50)
        BtnZoomOut.setGeometry(420, 70, 50, 50)
        BtnZoomIn.clicked.connect(self.increasefont)
        BtnZoomOut.clicked.connect(self.decreasefont)

        self.StackWidgetMain = QStackedWidget(self.WidgetMain)
        self.StackWidgetMain.setGeometry(0, 130, 480, 700)
        self.pageMethodUI()
        self.pageWhereUI()
        self.StackWidgetMain.addWidget(self.WidgetOrderMethod)
        self.StackWidgetMain.addWidget(self.WidgetEatWhere)
        self.StackWidgetMain.setCurrentWidget(self.WidgetOrderMethod)

        fontTitle, fontMiddle, _ = updateFontSize()
        self.BtnTakeout.setFont(fontMiddle)
        self.BtnHere.setFont(fontMiddle)
        self.BtnVoiceOrder.setFont(fontMiddle)
        self.BtnNormalOrder.setFont(fontMiddle)
        self.BtnRecommendOrder.setFont(fontMiddle)
        self.LabelWelcomeMain.setFont(fontTitle)

    def pageMethodUI(self):
        self.WidgetOrderMethod = QWidget(self.StackWidgetMain)
        self.WidgetOrderMethod.setFixedSize(480, 700)
        FrameOrderMethod = QFrame(self.WidgetOrderMethod)
        FrameOrderMethod.setGeometry(QRect(0, 10, 480, 660))
        LayoutOrderMethod = QGridLayout(FrameOrderMethod)

        self.BtnNormalOrder = makeBtn(440, 190, "일반 주문", FrameOrderMethod)
        self.BtnVoiceOrder = makeBtn(440, 190, "음성 주문", FrameOrderMethod)
        self.BtnRecommendOrder = makeBtn(440, 190, "메뉴 추천", FrameOrderMethod)
        # 각 주문방법 버튼 클릭하면 다음단계로 이동
        self.BtnNormalOrder.clicked.connect(lambda: self.selectOrderMethod("일반 주문"))
        self.BtnVoiceOrder.clicked.connect(lambda: self.selectOrderMethod("음성 주문"))
        self.BtnRecommendOrder.clicked.connect(lambda: self.selectOrderMethod("메뉴 추천"))

        LayoutOrderMethod.addWidget(self.BtnNormalOrder, 0, 0)
        LayoutOrderMethod.addWidget(self.BtnVoiceOrder, 1, 0)
        LayoutOrderMethod.addWidget(self.BtnRecommendOrder, 2, 0)
        LayoutOrderMethod.setVerticalSpacing(45)

    def pageWhereUI(self):
        self.WidgetEatWhere = QWidget(self.StackWidgetMain)
        self.WidgetEatWhere.setFixedSize(480, 700)

        self.BtnBack = makeBtn(50, 50, "홈", self.WidgetEatWhere)
        self.BtnBack.setGeometry(10, 0, 50, 50)
        self.BtnBack.clicked.connect(self.funHome)
        self.BtnHere = makeBtn(210, 500, "먹고가기", self.WidgetEatWhere)
        self.BtnHere.setGeometry(25, 140, 200, 500)
        self.BtnHere.clicked.connect(lambda: self.selectEatWhere("먹고가기"))
        self.BtnTakeout = makeBtn(210, 500, "포장하기", self.WidgetEatWhere)
        self.BtnTakeout.setGeometry(255, 140, 200, 500)
        self.BtnTakeout.clicked.connect(lambda: self.selectEatWhere("포장하기"))
        self.eatWhere = ""

    def selectOrderMethod(self, method):
        self.order_method = method
        print(f"선택한 주문 방법: {self.order_method}")
        self.StackWidgetMain.setCurrentWidget(self.WidgetEatWhere)

    def selectEatWhere(self, eatwhere):
        self.eatWhere = eatwhere
        print(f"선택한 식사 위치: {self.eatWhere}")
        if self.order_method == "음성 주문":
            print("음성 주문으로 이동합니다.")
            from VoiceOrder import VoiceOrder
            self.VoiceOrder = VoiceOrder()
            self.VoiceOrder.show()
        elif self.order_method == "메뉴 추천":
            print("메뉴 추천으로 이동합니다.")
            from RecommendOrder import RecommendOrder
            self.RecommendOrder = RecommendOrder()
            self.RecommendOrder.show()
        elif self.order_method == "일반 주문":
            print("일반 주문으로 이동합니다.")
            from NormalOrder import NormalOrder
            self.NormalOrder = NormalOrder()
            self.NormalOrder.show()

    def updateFont(self):
        fontTitle, fontMiddle, fontSmall = updateFontSize()
        self.BtnTakeout.setFont(fontMiddle)
        self.BtnHere.setFont(fontMiddle)
        self.BtnVoiceOrder.setFont(fontMiddle)
        self.BtnNormalOrder.setFont(fontMiddle)
        self.BtnRecommendOrder.setFont(fontMiddle)
        self.LabelWelcomeMain.setFont(fontTitle)

    def increasefont(self):
        Count = getCount()
        if Count < 5:
            setCount(Count + 1)
            fontTitle, fontMiddle, fontSmall = updateFontSize()
            fontTitle.setPointSize(fontTitle.pointSize() + 1)
            fontMiddle.setPointSize(fontMiddle.pointSize() + 1)
            fontSmall.setPointSize(fontSmall.pointSize() + 1)
            self.updateFont()

    def decreasefont(self):
        Count = getCount()
        if Count > -5:
            setCount(Count - 1)
            fontTitle, fontMiddle, fontSmall = updateFontSize()
            fontTitle.setPointSize(fontTitle.pointSize() - 1)
            fontMiddle.setPointSize(fontMiddle.pointSize() - 1)
            fontSmall.setPointSize(fontSmall.pointSize() - 1)
            self.updateFont()

    def funHome(self):
        self.order_method = ""
        self.eatWhere = ""
        self.StackWidgetMain.setCurrentWidget(self.WidgetOrderMethod)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomerMain()
    window.show()
    sys.exit(app.exec_())

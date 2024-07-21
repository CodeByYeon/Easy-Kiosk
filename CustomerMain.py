import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

fontTitle = QFont("SUITE SEMI Bold", 35)
fontMiddle = QFont("SUITE",25)
fontSmall = QFont("SUITE",16)
fontCount = 0

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(u"Background-color:rgb(255, 255, 255);")
        self.setFixedSize(480, 830)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.order_method = ""  # 주문 방법을 저장할 변수
        self.makeStackUI()

    def makeStackUI(self):
        self.WidgetMain = QWidget(self)
        self.setCentralWidget(self.WidgetMain)
        self.WidgetMain.setFixedSize(480, 830)

        self.LabelWelcomeMain = makeLabel(350, 85, "선택해주세요", self.WidgetMain)
        self.LabelWelcomeMain.setGeometry(10, 35, 350, 85)

        def makezoom(text):
            # 텍스트 크기 조절하는 버튼 생성
            btn = QPushButton()
            btn.setFixedSize(50, 50)
            btn.setStyleSheet(
                u"border: 1px solid rgba(0,0,0,0); border-radius: 10px; Background-color: rgb(255,126,0);font-weight:Bold; color: white; font-size: 40px;")
            btn.setText(text)
            btn.setParent(self.WidgetMain)
            return btn

        LabelZoom = makeLabel(105, 30, "글씨 크기", self.WidgetMain)
        LabelZoom.setGeometry(365, 35, 105, 30)

        BtnZoomIn = makezoom("+")
        BtnZoomOut = makezoom("-")
        BtnZoomIn.setGeometry(365, 70, 50, 50)
        BtnZoomOut.setGeometry(420, 70, 50, 50)
        BtnZoomIn.clicked.connect(self.increasefont)
        BtnZoomOut.clicked.connect(self.decreasefont)


        # 바탕이 되는 스택위젯 생성
        self.StackWidgetMain = QStackedWidget(self.WidgetMain)
        self.StackWidgetMain.setGeometry(0, 130, 480, 700)
        self.pageMethodUI()
        self.pageWhereUI()
        self.StackWidgetMain.addWidget(self.WidgetOrderMethod)
        self.StackWidgetMain.addWidget(self.WidgetEatWhere)
        self.StackWidgetMain.setCurrentWidget(self.WidgetOrderMethod)

        self.BtnTakeout.setFont(fontMiddle)
        self.BtnHere.setFont(fontMiddle)
        self.VoiceOrderbtn.setFont(fontMiddle)
        self.NormalOrderbtn.setFont(fontMiddle)
        self.RecommendOrderbtn.setFont(fontMiddle)
        self.LabelWelcomeMain.setFont(fontTitle)

    def pageMethodUI(self):
        # 첫번째 페이지
        self.WidgetOrderMethod = QWidget(self.StackWidgetMain)
        self.WidgetOrderMethod.setFixedSize(480, 700)
        FrameOrderMethod = QFrame(self.WidgetOrderMethod)
        FrameOrderMethod.setGeometry(QRect(0, 10, 480, 660))
        LayoutOrderMethod = QGridLayout(FrameOrderMethod)

        self.NormalOrderbtn = makeBtn(440, 190, "일반 주문", FrameOrderMethod)
        self.VoiceOrderbtn = makeBtn(440, 190, "음성 주문", FrameOrderMethod)
        self.RecommendOrderbtn = makeBtn(440, 190, "메뉴 추천", FrameOrderMethod)

        # 버튼에 클릭 이벤트 연결
        self.NormalOrderbtn.clicked.connect(lambda: self.selectOrderMethod("일반 주문"))
        self.VoiceOrderbtn.clicked.connect(lambda: self.selectOrderMethod("음성 주문"))
        self.RecommendOrderbtn.clicked.connect(lambda: self.selectOrderMethod("메뉴 추천"))

        LayoutOrderMethod.addWidget(self.NormalOrderbtn, 0, 0)
        LayoutOrderMethod.addWidget(self.VoiceOrderbtn, 1, 0)
        LayoutOrderMethod.addWidget(self.RecommendOrderbtn, 2, 0)
        LayoutOrderMethod.setVerticalSpacing(45)

    def pageWhereUI(self):
        # 두번째 페이지
        self.WidgetEatWhere = QWidget(self.StackWidgetMain)
        self.WidgetEatWhere.setFixedSize(480, 700)

        self.BtnHere = makeBtn(210, 500, "먹고가기", self.WidgetEatWhere)
        self.BtnHere.setGeometry(25, 140, 200, 500)
        self.BtnHere.clicked.connect(lambda: self.selectEatWhere("먹고가기"))
        self.BtnTakeout = makeBtn(210, 500, "포장하기", self.WidgetEatWhere)
        self.BtnTakeout.setGeometry(255, 140, 200, 500)
        self.BtnTakeout.clicked.connect(lambda: self.selectEatWhere("포장하기"))
        self.eatWhere = ""

    def selectOrderMethod(self, method):
        self.order_method = method  # 선택한 주문 방법 저장
        print(f"선택한 주문 방법: {self.order_method}")  # 콘솔에 출력 (테스트용)
        self.StackWidgetMain.setCurrentWidget(self.WidgetEatWhere)  # 두 번째 페이지로 전환

    def selectEatWhere(self,eatwhere):
        self.eatWhere = eatwhere
        print(f"선택한 식사 위치: {self.eatWhere}") # 콘솔에 출력
        if self.order_method == "음성 주문" :
            print(f"음성 주문으로 이동합니다.")
        elif self.order_method == "메뉴 추천" :
            print(f"메뉴 추천으로 이동합니다.")
        elif self.order_method == "일반 주문" :
            print(f"일반 주문으로 이동합니다.")


    def updateFont(self):
        self.BtnTakeout.setFont(fontMiddle)
        self.BtnHere.setFont(fontMiddle)
        self.VoiceOrderbtn.setFont(fontMiddle)
        self.NormalOrderbtn.setFont(fontMiddle)
        self.RecommendOrderbtn.setFont(fontMiddle)
        self.LabelWelcomeMain.setFont(fontTitle)

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
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작
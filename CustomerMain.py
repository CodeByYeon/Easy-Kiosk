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

        LabelWelcomeMain = makeLabel(350, 85, "선택해주세요", self.WidgetMain)
        LabelWelcomeMain.setGeometry(10, 35, 350, 85)
        LabelWelcomeMain.setFont(QFont("Arial", 39))

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
        LabelZoom.setFont(QFont("Arial", 19))
        LabelZoom.setGeometry(365, 35, 105, 30)

        BtnZoomIn = makezoom("+")
        BtnZoomOut = makezoom("-")
        BtnZoomIn.setGeometry(365, 70, 50, 50)
        BtnZoomOut.setGeometry(420, 70, 50, 50)

        # 바탕이 되는 스택위젯 생성
        self.StackWidgetMain = QStackedWidget(self.WidgetMain)
        self.StackWidgetMain.setGeometry(0, 130, 480, 700)
        self.pageMethodUI()
        self.pageWhereUI()
        self.StackWidgetMain.addWidget(self.WidgetOrderMethod)
        self.StackWidgetMain.addWidget(self.WidgetEatWhere)
        self.StackWidgetMain.setCurrentWidget(self.WidgetOrderMethod)

    def pageMethodUI(self):
        # 첫번째 페이지
        self.WidgetOrderMethod = QWidget(self.StackWidgetMain)
        self.WidgetOrderMethod.setFixedSize(480, 700)
        FrameOrderMethod = QFrame(self.WidgetOrderMethod)
        FrameOrderMethod.setGeometry(QRect(0, 10, 480, 660))
        LayoutOrderMethod = QGridLayout(FrameOrderMethod)

        NormalOrderbtn = makeBtn(440, 190, "일반 주문", FrameOrderMethod)
        VoiceOrderbtn = makeBtn(440, 190, "음성 주문", FrameOrderMethod)
        RecommendOrderbtn = makeBtn(440, 190, "메뉴 추천", FrameOrderMethod)

        # 버튼에 클릭 이벤트 연결
        NormalOrderbtn.clicked.connect(lambda: self.selectOrderMethod("일반 주문"))
        VoiceOrderbtn.clicked.connect(lambda: self.selectOrderMethod("음성 주문"))
        RecommendOrderbtn.clicked.connect(lambda: self.selectOrderMethod("메뉴 추천"))

        LayoutOrderMethod.addWidget(NormalOrderbtn, 0, 0)
        LayoutOrderMethod.addWidget(VoiceOrderbtn, 1, 0)
        LayoutOrderMethod.addWidget(RecommendOrderbtn, 2, 0)
        LayoutOrderMethod.setVerticalSpacing(45)

    def pageWhereUI(self):
        # 두번째 페이지
        self.WidgetEatWhere = QWidget(self.StackWidgetMain)
        self.WidgetEatWhere.setFixedSize(480, 700)

        BtnHere = makeBtn(210, 500, "먹고가기", self.WidgetEatWhere)
        BtnTakeout = makeBtn(210, 500, "포장하기", self.WidgetEatWhere)
        BtnHere.setGeometry(25, 140, 200, 500)
        BtnTakeout.setGeometry(255, 140, 200, 500)

    def selectOrderMethod(self, method):
        self.order_method = method  # 선택한 주문 방법 저장
        print(f"선택한 주문 방법: {self.order_method}")  # 콘솔에 출력 (테스트용)
        self.StackWidgetMain.setCurrentWidget(self.WidgetEatWhere)  # 두 번째 페이지로 전환


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작
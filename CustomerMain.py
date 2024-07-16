import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def makezoom(text):
    #텍스트 크기 조절하는 버튼 생성
    btn = QPushButton()
    btn.setFixedSize(60, 60)
    btn.setStyleSheet(
        u"border: 1px solid rgba(0,0,0,0); border-radius: 16px; Background-color: rgb(255,126,0);font-weight:Bold; color: white; font-size: 90px;")
    btn.setText(text)
    return btn

def btnmake(w,h,text,parents):
    #버튼 생성하는 함수
    btn = QPushButton()
    btn.setFixedSize(w, h)
    btn.setText(text)
    btn.setParents(parents)
    btn.setFlat(1)
    return btn

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(u"Background-color:rgb(255, 255, 255);")
        self.setFixedSize(480,830)
        self.setWindowFlags(Qt.FramelessWindowHint)

        #바탕이 되는 스택위젯 생성
        self.StackWidgetMain = QStackedWidget(self)
        self.setCentralWidget(self.StackWidgetMain)
        self.StackWidgetMain.setFixedSize(480,830)

        #첫번째 페이지
        self.WidgetEatWhere = QWidget(self.StackWidgetMain)
        self.WidgetEatWhere.setFixedSize(480,830)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작
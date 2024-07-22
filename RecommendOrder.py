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
class RecommendOrder(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecommendOrder()
    window.show()
    sys.exit(app.exec_())  # 이벤트 루프 시작
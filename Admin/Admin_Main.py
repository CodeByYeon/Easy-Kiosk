import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Admin_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('키오스크 관리자')
        self.setFixedSize(480,830)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.WidgetAdminMenu = QWidget()
        self.WidgetAdminMenu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setCentralWidget(self.WidgetAdminMenu)
        managerLabel = QLabel("관리자 메뉴", self)
        managerLabel.setFont(QFont("Noto Sans CJK KR Bold", 30))
        managerLabel.setAlignment(Qt.AlignCenter)
        managerLabel.setGeometry(100, 40, 280, 40)
        btnContainer = QFrame(self.WidgetAdminMenu)
        btnContainer.setGeometry(20, 90, 440, 600)
        btnContainer.setFixedSize(440, 600)
        btngrid = QGridLayout(btnContainer)
        btngrid.setVerticalSpacing(20)
        btngrid.setHorizontalSpacing(10)

        add_menu_button = self.create_button("ad-menuadd.png")
        #add_menu_button.clicked.connect(self.add_menu)
        update_menu_button = self.create_button("ad-menuedit.png")
        #update_menu_button.clicked.connect(self.update_menu)
        delete_menu_button = self.create_button("ad-menudel.png")
        #delete_menu_button.clicked.connect(self.delete_menu)
        setting_button = self.create_button("ad-set.png")
        #setting_button.clicked.connect(self.go_to_settingwindow)

        btngrid.addWidget(add_menu_button, 0, 0)
        btngrid.addWidget(update_menu_button, 0, 1)
        btngrid.addWidget(delete_menu_button, 1, 0)
        btngrid.addWidget(setting_button, 1, 1)

        exit_button = QPushButton("나       가       기", self)
        exit_button.setGeometry(30, 710, 420, 90)
        exit_button.setStyleSheet(
            "background-color: rgb(255,255,255);border: 4px solid rgb(255,136,0); color: rgb(255,136,0);")
        exit_button.setFont(QFont("Noto Sans CJK KR Black", 40))

    def create_button(self, image_path):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn = QPushButton()
        # 이미지를 버튼의 배경으로 설정하고, 이미지 크기를 버튼 크기에 맞게 조정
        btn.setSizePolicy(sizePolicy)
        btn.setStyleSheet(
            f"QPushButton {{ background-image: url('img/AdminUI/{image_path}');"
            f"background-position: center;"
            f"background-repeat: no-repeat;"
            f"background-size: cover;"
            f" border-radius: 5px;  "
            f"border : 4px solid rgb(255,126,0)}}")
        btn.setFlat(True)
        return btn

    def exit_admin_window(self):
        self.close()  # 현재 창을 닫음

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_window = Admin_Main()
    admin_window.show()
    sys.exit(app.exec_())
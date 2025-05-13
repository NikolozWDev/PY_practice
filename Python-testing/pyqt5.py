# PyQt5 GUI intro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('main_server')
        self.setGeometry(700, 300, 500, 400)
        self.setWindowIcon(QIcon('assets/folder_92613.jpg'))

        label = QLabel('Error Server', self)
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet('color: red; font-size: 30px; font-weight: bold; background-color: black;')
        label.setAlignment(Qt.AlignCenter)
        label.setAlignment(Qt.AlignHCenter)

        label2 = QLabel(self)
        label2.setGeometry(300, 300, 500, 100)
        pixmap = QPixmap('assets/folder_92613.jpg')
        label2.setPixmap(pixmap)
        label2.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# start
main()
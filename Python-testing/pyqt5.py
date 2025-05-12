# PyQt5 GUI intro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('main_server')
        self.setGeometry(700, 300, 500, 400)
        self.setWindowIcon(QIcon('assets/folder_92613.jpg'))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# start
main()
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("TayPyside Example")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.setGeometry(300, 300, 300, 300)
        self.welcomeText = QLabel(self)
        self.welcomeText.setFocus="true"
        self.welcomeText.setText("Welcome to the PySide6 application. This application demonstrates the power ofPySide6 for making accessible GUI apps with python. Press next to continue.")
        self.grid.addWidget(self.welcomeText, 0, 0)
        self.nextButton = QPushButton(self)
        self.nextButton.setText("Next")
        self.nextButton.setShortcut("Alt+N")
        self.grid.addWidget(self.nextButton,1,2)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("TayPyside Example")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.welcomeText = QLabel(self)
        self.welcomeText.setFocus="true"
        self.welcomeText.setText("Welcome to the PySide6 application. This application demonstrates the power ofPySide6 for making accessible GUI apps with python. Press next to continue.")
        self.grid.addWidget(self.welcomeText, 0, 0)
        self.nextButton = QPushButton(self)
        self.nextButton.setText("Next")
        self.nextButton.setShortcut("Alt+N")
        self.grid.addWidget(self.nextButton,1,2)
        applicationMenu = self.menuBar()
        file = applicationMenu.addMenu("File")
        file.addAction("New")
        save = QAction("Save",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        edit = applicationMenu.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("Quit",self) 
        file.addAction(quit)
        self.setMenuBar(applicationMenu)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
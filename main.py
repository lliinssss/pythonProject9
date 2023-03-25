import PyQt6
from PyQt6.QtWidgets import QMainWindow, QApplication
from reg_win import Ui_reg_win
from new_window import Ui_new_window
import sys


class RegWindow(QMainWindow, Ui_reg_win):
    def __init__(self):
        super(RegWindow, self).__init__()
        self.setupUi(self)


class NewWindow(QMainWindow, Ui_new_window):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
reg_win = RegWindow()
new_window = NewWindow()
new_window.show()
reg_win.show()
app.exec()

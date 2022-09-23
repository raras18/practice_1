"""
Project Name: MoilApps Templates
Writer : Haryanto
PROJECT MADE WITH: Qt Designer
Build for: MOIL-LAB
Copyright: MOIL-2022

This project can be use a a template to create better user interface when you design a project.

There are limitations on Qt licenses if you want to use your products
commercially, I recommend reading them on the official website:
https://doc.qt.io/qtforpython/licenses.html

"""
import sys
from model import Model
from controller import Controller
from view import View

try:
    from PyQt6.QtWidgets import QApplication, QMainWindow
    pyqt_version = "pyqt6"

except:
    from PyQt5.QtWidgets import QApplication, QMainWindow
    pyqt_version = "pyqt5"


class App:
    def __init__(self, parent):
        self.model = Model()
        self.main_ctrl = Controller(self.model)
        self.main_view = View(parent, self.model, self.main_ctrl)


if __name__ == "__main__":
    apps = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = App(MainWindow)
    MainWindow.show()
    sys.exit(apps.exec())
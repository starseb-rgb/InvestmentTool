import menu_choose
from loading_screen import LoadingScreen
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
import sys


# start all the GUIs

if __name__ == "__main__":
    # start application
    app = QApplication(sys.argv)

    # create main window and show it
    # main = menu_choose.Chart_GUI()
    # main.show()

    # create chart window and show it
    MainWindow = QtWidgets.QMainWindow()
    chart = menu_choose.Ui_Menu_Choose()
    chart.setupUi(MainWindow)
    MainWindow.show()

    # create loading screen and show it
    MainWindow2 = QtWidgets.QMainWindow()
    load = LoadingScreen()
    load.setup(MainWindow2)
    MainWindow2.show()

    sys.exit(app.exec_())


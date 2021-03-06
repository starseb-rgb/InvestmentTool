########################################
# run 'main.py' to execute the project #
########################################

import menu_choose
from loading_screen import LoadingScreen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

# start all the GUIs

if __name__ == "__main__":
    # start application
    app = QApplication(sys.argv)

    # if the next windows are not appearing if you press any buttons than remove all of the # below
    # this will start all the files manually from this main file

    # create chart window and show it
    # MainWindow = QtWidgets.QMainWindow()
    # chart = menu_choose.Ui_Menu_Choose()
    # chart.setupUi(MainWindow)
    # MainWindow.show()

    # create loading screen and show it
    load = LoadingScreen()
    load.startLoadingScreen()

    sys.exit(app.exec_())
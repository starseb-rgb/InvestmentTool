import menu_choose
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

import sys


# start all the GUIs
if __name__ == "__main__":
    # start application
    app = QApplication(sys.argv)

    # start chart
    main = menu_choose.Window()
    main.show()

    # start
    MainWindow = QtWidgets.QMainWindow()
    ui = menu_choose.Ui_Menu_Choose()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

    # btc = Chart('bitcoin', 'eur', '1448150400', '1606003200', 15, 200)
    # arr = btc.callAPI()
    # print(arr[0])


    # sample data: 01/01/2020 --> 1577836800    01/02/2020 --> 1580515200
    # sample data: 01/11/2020 --> 1604188800    22/11/2020 --> 1606003200
    # sample data: 22/11/2015 --> 1448150400

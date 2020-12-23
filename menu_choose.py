# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_choose = QtWidgets.QFrame(self.centralwidget)
        self.menu_choose.setGeometry(QtCore.QRect(60, 20, 651, 441))
        self.menu_choose.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_choose.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_choose.setObjectName("menu_choose")
        self.frame_data_pic = QtWidgets.QFrame(self.menu_choose)
        self.frame_data_pic.setGeometry(QtCore.QRect(-10, -50, 651, 541))
        self.frame_data_pic.setStyleSheet("image: url(:/newPrefix/System Development/10.jpg);\n"
"background-color: rgb(0, 0, 0);")
        self.frame_data_pic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_data_pic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data_pic.setObjectName("frame_data_pic")
        self.frame = QtWidgets.QFrame(self.menu_choose)
        self.frame.setGeometry(QtCore.QRect(0, 230, 641, 201))
        self.frame.setStyleSheet("background-color: rgb(16, 16, 16);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.combo_currency = QtWidgets.QComboBox(self.frame)
        self.combo_currency.setGeometry(QtCore.QRect(390, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_currency.setFont(font)
        self.combo_currency.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.combo_currency.setObjectName("combo_currency")
        self.combo_currency.addItem("")
        self.combo_currency.addItem("")
        self.combo_crypto = QtWidgets.QComboBox(self.frame)
        self.combo_crypto.setGeometry(QtCore.QRect(390, 120, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_crypto.setFont(font)
        self.combo_crypto.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.combo_crypto.setObjectName("combo_crypto")
        self.combo_crypto.addItem("")
        self.combo_crypto.addItem("")
        self.label_currency = QtWidgets.QLabel(self.frame)
        self.label_currency.setGeometry(QtCore.QRect(30, 50, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_currency.setFont(font)
        self.label_currency.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: 3px solid rgb(0, 170, 0);\n"
"border-radius: 50px;")
        self.label_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currency.setObjectName("label_currency")
        self.label_currency_2 = QtWidgets.QLabel(self.frame)
        self.label_currency_2.setGeometry(QtCore.QRect(30, 120, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_currency_2.setFont(font)
        self.label_currency_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_currency_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currency_2.setObjectName("label_currency_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(560, 180, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.menu_choose)
        self.label.setGeometry(QtCore.QRect(120, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 170, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_currency.setItemText(0, _translate("MainWindow", "Euro (€)"))
        self.combo_currency.setItemText(1, _translate("MainWindow", "Dollar ($)"))
        self.combo_crypto.setItemText(0, _translate("MainWindow", "Bitcoin "))
        self.combo_crypto.setItemText(1, _translate("MainWindow", "Ethereum "))
        self.label_currency.setText(_translate("MainWindow", "Choose your Currency"))
        self.label_currency_2.setText(_translate("MainWindow", "Choose your Cryptocurrency"))
        self.pushButton.setText(_translate("MainWindow", "OK "))
        self.label.setText(_translate("MainWindow", "Start the Investment Calculator"))
import big_data_pic_rc
import bitcoin_rc
import crypto_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize,
#                            QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient,
#                            QPalette, QPainter, QPixmap, QRadialGradient)
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QBasicTimer
from menu_choose import *

#loading screen
class LoadingScreen(object):

    def startLoadingScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.load = LoadingScreen()
        self.load.setup(self.window)
        #self.window.setGeometry(200,200,750,500)
        self.window.show()

    def startNewWindow(self):
        self.newWindow = QtWidgets.QMainWindow()
        self.mainWin = Ui_Menu_Choose()
        self.mainWin.setupUi(self.newWindow)
        self.newWindow.show()


    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropshadowFrame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.dropshadowFrame.setFont(font)
        self.dropshadowFrame.setStyleSheet("QFrame { \n"
                                           "background-color: rgb(0, 0, 0);\n"
                                           "    color: rgb(0, 170, 0);\n"
                                           "border radius: 10px;\n"
                                           "text-align:center;\n"
                                           "}\n"
                                           "QProgregressBar::chunk{\n"
                                           "border radius: 10px;\n"
                                           "background-color: qlineargradient(spread:pad, x1:0.0173182, y1:0.461, x2:0.994, y2:0.466, stop:0.0113636 rgba(101, 232, 14, 255), stop:0.994318 rgba(15, 116, 26, 255));\n"
                                           "}")
        self.dropshadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropshadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropshadowFrame.setObjectName("dropshadowFrame")
        self.label_heading = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_heading.setGeometry(QtCore.QRect(120, 90, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.label_heading.setFont(font)
        self.label_heading.setObjectName("label_heading")
        self.label_description = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_description.setGeometry(QtCore.QRect(80, 140, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.label_description.setFont(font)
        self.label_description.setObjectName("label_description")
        self.label = QtWidgets.QLabel(self.dropshadowFrame)
        self.label.setGeometry(QtCore.QRect(50, 30, 47, 14))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pic_label = QtWidgets.QLabel(self.dropshadowFrame)
        self.pic_label.setGeometry(QtCore.QRect(-10, -20, 766, 511))
        self.pic_label.setText("")
        self.pic_label.setPixmap(QtGui.QPixmap("green_electronic_frame.preview.jpg"))
        self.pic_label.setObjectName("pic_label")
        self.startButton = QtWidgets.QPushButton(self.dropshadowFrame)
        self.startButton.setGeometry(QtCore.QRect(350, 340, 75, 23))
        self.startButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 170, 0);")
        self.startButton.setObjectName("startButton")




        self.startButton.clicked.connect(self.startNewWindow)
        # self.startButton.clicked.connect(self.close)

        self.label_2 = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_2.setGeometry(QtCore.QRect(110, 180, 561, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pic_label.raise_()
        self.label_heading.raise_()
        self.label_description.raise_()
        self.label.raise_()
        self.startButton.raise_()
        self.label_2.raise_()
        self.verticalLayout.addWidget(self.dropshadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        #QTimer-->START
        #self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(self.progress)
        #Timer in Milliseconds
        #self.timer.start(35)


    # def start(self):

        # if self.timer.isActive():
            # self.timer.stop()
        # else:
            # self.timer.start(100, self)

    # def timerEvent(self, event):
        # if self.step >= 100:
            # self.timer.stop()
            # self.startNewWindow()
            # return
        # self.step += 2
        # self.progressBar.setValue(self.step)


    # def progress(self):
        # self.completed = 0.0000
        # while self.completed < 100:
            # self.completed += 0.0001
            # self.progressBar.setValue(self.completed)

        # self.startNewWindow()

    ##########
    # we might need the code below at a later point
    ##########

    #def progress(self):
        #global counter

        #set value to progress bar
        #self.ui.progressBar.setValue(counter)

        #close loading screen and open app
        #if counter > 100:
            # stop timer
            #self.timer.stop()

            #show menu_choose
            #self.main= Menu_Choose()
            #self.main.show()


            #close splash screen
            #self.close()

        #Increase counter
        #counter += 1

    #def progress(self):
        #self.completed = 0.0000

        #while self.completed < 100:
            #self.completed += 0.0001
            #self.progressBar.setValue(self.completed)

        # self.completed.stop()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">YOUR Investment Tool</span></p></body></html>"))
        self.label_description.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; color:#00aa00;\">Make profitable investment decisions at the right time by using the Investment Calculator</span></p></body></html>"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">The crypto market has been one of the hottest,but also most volatile markets</p><p align=\"center\">since Bitcoin\'s whitepaper. It is not only difficult to make investment decisions, </p><p align=\"center\">but just as hard to keep track of all the different coins that have popped up in</p><p align=\"center\">the last few years.</p></body></html>"))

# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = LoadingScreen()
    # ui.setup(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
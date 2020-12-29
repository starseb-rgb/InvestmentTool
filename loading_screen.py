from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize,
                            QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5 import QtCore, QtGui, QtWidgets


#loading screen
class LoadingScreen(object):
    def __init__(self):
        self.ui = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
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
        self.label_heading.setGeometry(QtCore.QRect(10, 80, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.label_heading.setFont(font)
        self.label_heading.setObjectName("label_heading")
        self.label_description = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_description.setGeometry(QtCore.QRect(10, 140, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.label_description.setFont(font)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropshadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(40, 240, 581, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(10, 144, 41);\n"
"    color: rgb(16, 22, 136);\n"
"\n"
"border style:none;\n"
"border radius: 10px;\n"
"text-align:center;\n"
"}")
        self.progressBar.setProperty("value", 24 )
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(10, 260, 641, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.label_loading.setFont(font)
        self.label_loading.setObjectName("label_loading")
        self.label_creators = QtWidgets.QLabel(self.dropshadowFrame)
        self.label_creators.setGeometry(QtCore.QRect(460, 330, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.label_creators.setFont(font)
        self.label_creators.setObjectName("label_creators")
        self.verticalLayout.addWidget(self.dropshadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        #QTimer-->START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        #Timer in Milliseconds
        self.timer.start(35)


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

    def progress(self):
        self.completed = 0.0000

        while self.completed < 100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)

        # self.completed.stop()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">YOUR Investment Tool</span></p></body></html>"))
        self.label_description.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; color:#00aa00;\">Make profitable investment decisions at the right time by using the Investment Calculator</span></p></body></html>"))
        self.label_loading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; color:#ffffff;\">Loading ...</span></p></body></html>"))
        self.label_creators.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; vertical-align:sub;\">Created by Aaron, Sebastian and Anne-Catherine </span></p></body></html>"))
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from createChart import Chart
import datetime as dt
import calendar;
import time;
# from loading_screen import *
# import sys


##########################################################
# this file contains our 2 main GUI classes
##########################################################



# variable plot for not calling API until 'OK' button is clicked
plot = 0
# global variables crypto and currency to use the user input for API call (scroll further down for details)
crypto = ''
currency = ''


# the following class is for visualizing our data as an interactive chart
class Chart_GUI(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Chart_GUI, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)


        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def plot(self):
        # only generate chart if plot == 1 (plot is 1 if 'OK' is clicked)
        if plot == 1:
            # get current timestamp in order to receive most recent data
            ts = calendar.timegm(time.gmtime())
            timestamp = dt.datetime.fromtimestamp(ts)
            # for starting date we always use the same date, good starting point to learn about history of cryptos
            coin = Chart(crypto, currency, '1448150400', ts, 60, 200)
            data = coin.callAPI()

            date = data[0]
            price = data[1]

            # MA = moving average
            data = coin.calculateMA(price)
            movingAverageShort = data[0]
            movingAverageLong = data[1]

            data = coin.calculateInvestmentSignals(price, movingAverageShort, movingAverageLong)
            buyPrice = data[0]
            sellPrice = data[1]

            self.figure.clear()
            ax = self.figure.add_subplot(111)

            # plot data
            ax.plot(date, price, label='cryptocurrency')
            ax.plot(date, movingAverageShort, label='short term moving average')
            ax.plot(date, movingAverageLong, label='long term moving average')
            ax.scatter(date, buyPrice, label='Buy', marker='^', color='green', linewidths=3)
            ax.scatter(date, sellPrice, label='Sell', marker='v', color='red', linewidths=3)
            ax.set_title(crypto + ' last checked on: ' + str(timestamp))
            ax.set_xlabel('timespan')
            ax.set_ylabel(currency)
            ax.legend(loc='upper left')

            self.canvas.draw()

            # call the API every 60s to get new data
            self.timer = QtCore.QTimer()
            self.timer.setInterval(60000)
            self.timer.timeout.connect(self.plot)
            self.timer.start()


# the following class is collecting the user input we need to call the API, create objects and plot our chart
class Ui_Menu_Choose(object):

    # this functions converts the currencies into the required format to call the coingecko API (API call happens in Chart_GUI)
    def show(self):
        chosen_curr = self.combo_currency.currentText()
        if chosen_curr == 'Euro (€)':
            global currency
            currency = 'eur'
        elif chosen_curr == 'US Dollar ($)':
            currency = 'usd'

        crypto_input = self.combo_crypto.currentText()
        if crypto_input == 'Bitcoin ':
            global crypto
            crypto = 'bitcoin'
        elif crypto_input == 'Ethereum ':
            crypto = 'ethereum'
        elif crypto_input == 'Litecoin ':
            crypto = 'litecoin'
        elif crypto_input == 'Ripple ':
            crypto = 'ripple'

        self.chart = Chart_GUI()
        self.chart.show()



    # function to give a signal to plot the chart
    def displayChart(self):
        global plot
        plot = 1

    #def getCurrency(self):
    #    global currency
    #    return currency

    #def getCrypto(self):
    #    global crypto
    #    return crypto

    #def getPlot(self):
    #    global plot
    #    return plot


    # following code is mostly auto-generated by QT Designer but contains adjustments (e.g. call function when button is clicked)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 533)
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
        self.frame.setObjectName("frame_data_pic")
        self.label_photo = QtWidgets.QLabel(self.frame_data_pic)
        self.label_photo.setGeometry(QtCore.QRect(30, 90, 601, 191))
        self.label_photo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_photo.setText("")
        self.label_photo.setPixmap(QtGui.QPixmap("maxresdefault.jpg"))
        self.label_photo.setScaledContents(True)
        self.label_photo.setObjectName("label_photo")
        self.frame = QtWidgets.QFrame(self.menu_choose)
        self.frame.setGeometry(QtCore.QRect(0, 230, 641, 201))
        self.frame.setStyleSheet("background-color: rgb(16, 16, 16);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.combo_currency = QtWidgets.QComboBox(self.frame)
        self.combo_currency.setGeometry(QtCore.QRect(390, 50, 161, 21))
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

        # pass the user input to the function above -> creation of objects depending on user input
        self.pushButton.clicked.connect(self.displayChart)
        self.pushButton.clicked.connect(self.show)


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
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(60, 0, 75, 23))
        self.infoButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 170, 0);")
        self.infoButton.setObjectName("infoButton")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Investment Calculator"))
        self.combo_currency.setItemText(0, _translate("MainWindow", "Euro (€)"))
        self.combo_currency.setItemText(1, _translate("MainWindow", "US Dollar ($)"))
        self.combo_crypto.setItemText(0, _translate("MainWindow", "Bitcoin "))
        self.combo_crypto.setItemText(1, _translate("MainWindow", "Ethereum "))
        self.combo_crypto.setItemText(2, _translate("MainWindow", "Litecoin "))
        self.combo_crypto.setItemText(3, _translate("MainWindow", "Ripple "))
        self.label_currency.setText(_translate("MainWindow", "Choose your Currency"))
        self.label_currency_2.setText(_translate("MainWindow", "Choose your Cryptocurrency"))
        self.pushButton.setText(_translate("MainWindow", "OK "))
        self.label.setText(_translate("MainWindow", "Start the Investment Calculator"))
        self.infoButton.setText(_translate("MainWindow", "Info"))


        self.infoButton.clicked.connect(self.show_popup)

    def show_pic(self):
        self.label_photo.setPixmap(QtGui.QPixmap("maxresdefault.jpg"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Welcome to your INVESTMENT Tool!")
        msg.setText("Instructions for use:\n"
                    "- Choose a Currency\n"
                    "- Choose the Cryptocurrency you prefer\n"
                    "- Press the button 'OK' to confirm your choice\n"
                    "- Press the button 'Plot' in the second window")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.setDetailedText("This app is designed to support you making decisions at the right time. \nBased on a Dual-Crossing-Moving-Average-Crossover strategy, this app will signal you to BUY a self-choosen Asset as soon as the Short Term Average (7 days) crosses the Long Term Average (25 days) and rises above it, vice versa.\nThe app signals you to SELL as soon as the Short Term Average crosses the Long Term Average and falls below it.\nPlease note that this app does not guarantee any profits and is intended to act as a guide in the crypto market only.")

        x = msg.exec_()
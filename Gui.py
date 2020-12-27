
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize,
                            QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPalette, QPainter, QPixmap, QRadialGradient)

#loading screen
from loading_screen import Ui_MainWindow

#class loading screen
class LoadingScreen(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.ui= Ui_MainWindow
        self.ui.setupUi(self, Ui_MainWindow)



        #show window
        self.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadingScreen = QtWidgets.QMainWindow()
    ui = LoadingScreen
    LoadingScreen.show()
    sys.exit(app.exec_())
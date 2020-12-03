from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(586, 472)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 420, 101, 41))
        self.btn1.setObjectName("pushButton")
        self.widget1 = PlotWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 561, 401))
        self.widget1.setObjectName("widget")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Graph"))
        self.btn1.setText(_translate("mainWindow", "Do The Thing"))
from pyqtgraph import PlotWidget

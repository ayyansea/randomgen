from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 263)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.verticalLayout.addWidget(self.list1)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        self.graphWidget = pg.PlotWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "THE GENERATOR"))
        self.button1.setText(_translate("MainWindow", "Пупка"))

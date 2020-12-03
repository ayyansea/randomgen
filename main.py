from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt 
import matplotlib as mpl 
import pyqtgraph as pg
from graph import Ui_mainWindow
import sys

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.btn1.setFont(QtGui.QFont('Montserrat', 10))

        self.hour = [1,2,3,4,5]
        self.temperature = [10,20,30,40,50]

        self.ui.btn1.clicked.connect(self.doPlot(self.hour, self.temperature))

    def doPlot(self, h, t):
        graph.QtWidgets('widget')

app = QtWidgets.QApplication(sys.argv)
form = myWindow()
form.show()
app.exec_()
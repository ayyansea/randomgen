from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg 
import numpy as np
import sys
import os

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('main_better.ui', self)
        self.x = [1,2,3]
        self.y = [1,10,25]
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.butt)

    def plot(self, hour, temperature):
        self.widget.plot(hour, temperature)

    @pyqtSlot()
    def on_click(self):
        self.plot(self.x, self.y)
    def butt(self):
        self.widget.clear()
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
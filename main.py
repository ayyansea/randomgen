from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt 
import matplotlib as mpl 
import ui
import sys

mpl.use("Qt5Agg")

app = QtWidgets.QApplication([])
win = uic.loadUi('main.ui')

win.show()
sys.exit(app.exec())


from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt 
import matplotlib as mpl 

def btn_click1():
    alert = QMessageBox()
    alert.setText('Button 1 clicked!')
    alert.exec()

def btn_click2():
    alert = QMessageBox()
    alert.setText('Button 2 clicked!')
    alert.exec()

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button1 = QPushButton('One')
button2 = QPushButton('Two')
layout.addWidget(button1)
layout.addWidget(button2)
button1.clicked.connect(btn_click1)
button2.clicked.connect(btn_click2)
window.setLayout(layout)
window.show()
app.exec_()


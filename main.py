from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg 
import numpy as np
import sys
import os
import rand

#определяем класс основного окна
class MainWindow(QMainWindow):

    #конструктор
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('main_better.ui', self)
        self.pushButton.clicked.connect(self.even)
        self.pushButton_2.clicked.connect(self.normal)

    #функция, выводящая график необходимого нам распределения
    #widget - контейнер для графика, описанный в main.ui
    def plot(self, x):
        self.widget.addItem(x)

    #описываем действия для кнопок
    @pyqtSlot()
    def even(self):  
        #равномерное распределение
        #spinBox.value() - значение поля "Количество величин"
        self.n = self.spinBox.value()
        #x1 - координаты каждого из столбцов графика 
        self.x1 = np.arange(self.spinBox.value())
        #убираем то, что было нарисовано ранее
        self.widget.clear()
        #заполняем массив (лист) a случайными величинами
        self.a = []
        for i in range(self.n):
            #even - функция равномерного распределения из файла rand.py
            #принимает два аргумента: min и max, то есть диапазон значений, 
            #которые может принимать случайная величина
            self.a.append(rand.even(0,1))
        #создаем столбчатую диаграмму на основе ранее определенных массивов
        #для каждого столбца с координатой из массива x1 мы определяем соответствующую высоту a
        #a, в свою очередь, является значением случайной величины
        #width - ширина каждого отдельного столбца
        #brush - цвет столбцов, 'w' - белый
        self.bg1 = pg.BarGraphItem(x=self.x1+0.5, height=self.a, width=0.5, brush='w')
        #рисуем график
        self.plot(self.bg1)
    def normal(self):
        #здесь и далее принцип такой же, как и в функции выше
        self.n = self.spinBox.value()
        self.x1 = np.arange(self.spinBox.value())
        self.widget.clear()
        self.a = []
        for i in range(self.n):
            #normal - функция нормального распределения из файла rand.py
            #   не принимает аргументов
            self.a.append(rand.normal())
        self.bg1 = pg.BarGraphItem(x=self.x1+0.5, height=self.a, width=1, brush='w')
        self.plot(self.bg1)
    
def main():
    #создаем объект класса MainWindow и показываем основное окно
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
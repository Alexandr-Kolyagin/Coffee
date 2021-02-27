import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()

        self.coffe_sorts = cur.execute("""SELECT Name FROM coffee""").fetchall()
        self.coffe_description = cur.execute("""SELECT * FROM coffee""").fetchall()
        print(self.coffe_sorts)
        print(self.coffe_description)
        # self.groupBox.hide()
        self.clear_btn.clicked.connect(self.groupBox.hide)
        self.degres_of_roasting = {1: 'Слабая', 2: 'Средняя', 3: 'Сильная'}

        x = 30
        y = 40
        for sort in self.coffe_sorts:
            self.btn = QPushButton(sort[0], self)
            self.btn.resize(180, 40)
            self.btn.move(x, y)
            self.btn.clicked.connect(self.btn_click)
            self.btn.setStyleSheet(".QPushButton{border-radius: 20}")
            y += 45

        con.commit()

    def btn_click(self):
        try:
            self.groupBox.show()
            sender = self.sender().text()
            index = self.coffe_sorts.index((sender,))
            self.name.setText('Название сорта: ' + self.coffe_description[index][0])
            self.degree_of_roasting.setText('Степень обжарки: ' + self.degres_of_roasting[self.coffe_description[index][1]])
            self.shredded.setText('Вид: ' + 'молотый' if self.coffe_description[index][2] else 'зерновой')
            self.taste.setText('Описание вкуса: ' + self.coffe_description[index][3])
            self.price.setText('Цена: ' + str(self.coffe_description[index][4]) + 'р')
            self.package_volume_grams.setText('Объем: ' + str(self.coffe_description[index][5]) + "г")
        except Exception as ex:
            print(type(ex).__name__)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

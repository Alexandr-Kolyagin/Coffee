import sqlite3
import sys

from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.clear_btn.clicked.connect(self.groupBox.hide)
        self.add_btn.clicked.connect(self.add_sort)
        self.update_btn.clicked.connect(self.update)
        self.degres_of_roasting = {1: 'Слабая', 2: 'Средняя', 3: 'Сильная'}

        self.coffe_sorts = self.cur.execute("""SELECT Name FROM coffee""").fetchall()
        self.coffe_description = self.cur.execute("""SELECT * FROM coffee""").fetchall()



        x = 30
        y = 40
        self.buttons = []
        for sort in self.coffe_sorts:
            self.btn = QPushButton(sort[0], self)
            self.btn.resize(180, 40)
            self.btn.move(x, y)
            self.btn.clicked.connect(self.btn_click)
            self.btn.setStyleSheet(".QPushButton{border-radius: 20}")
            self.buttons.append(self.btn)
            y += 45

        self.con.commit()
    def update(self):
        for btn in self.buttons:
            btn.hide()
        self.coffe_sorts = self.cur.execute("""SELECT Name FROM coffee""").fetchall()
        self.coffe_description = self.cur.execute("""SELECT * FROM coffee""").fetchall()

        x = 30
        y = 40
        self.buttons = []
        for sort in self.coffe_sorts:
            self.btn = QPushButton(sort[0], self)
            self.btn.resize(180, 40)
            self.btn.move(x, y)
            self.btn.clicked.connect(self.btn_click)
            self.btn.setStyleSheet(".QPushButton{border-radius: 20}")
            self.btn.show()
            self.buttons.append(self.btn)
            y += 45

    def btn_click(self):
        try:
            self.groupBox.show()
            sender = self.sender().text()
            index = self.coffe_sorts.index((sender,))
            self.name.setText('Название сорта: ' + self.coffe_description[index][0])
            self.degree_of_roasting.setText(
                'Степень обжарки: ' + self.degres_of_roasting[self.coffe_description[index][1]])
            self.shredded.setText('Вид: ' + 'молотый' if self.coffe_description[index][2] else 'Вид: ' + 'зерновой')
            self.taste.setText('Описание вкуса: ' + self.coffe_description[index][3])
            self.price.setText('Цена: ' + str(self.coffe_description[index][4]) + 'р')
            self.package_volume_grams.setText('Объем: ' + str(self.coffe_description[index][5]) + "г")
        except Exception as ex:
            print(type(ex).__name__)

    def add_sort(self):
        self.add_coffee = AddCoffee()
        self.add_coffee.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.add_coffee.show()


class AddCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        # self.degres_of_roasting = {'Слабая': 1, 'Средняя': 2, 'Сильная': 3}

        self.add_sort_btn.clicked.connect(self.add_sort)
        self.cancel_btn.clicked.connect(self.hide)

        self.con.commit()

    def add_sort(self):
        try:
            self.name_coffee = self.name.text()
            self.degree_of_roasting_coffee = int(self.degree_of_roasting.text())
            self.shredded_coffee = True if self.shredded.text().lower() == "молотый" else False
            self.taste_coffee = self.taste.text()
            self.price_coffee = int(self.price.text())
            self.package_volume_grams_coffee = int(self.package_volume_grams.text())
            line = f"""INSERT INTO coffee(Name, degree_of_roasting, shredded, taste, price, package_volume_grams) VALUES{

            self.name_coffee,
            self.degree_of_roasting_coffee,
            self.shredded_coffee,
            self.taste_coffee,
            self.price_coffee,
            self.package_volume_grams_coffee

            } """
            self.cur.execute(line)
            self.con.commit()

        except Exception as ex:
            print(type(ex))
            print("Неверный формат ввода!")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

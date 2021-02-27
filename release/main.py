import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('main.ui', self)

        self.setupUi(self)

        self.con = sqlite3.connect("data/coffee.sqlite")
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 661)
        font = QtGui.QFont()
        font.setPointSize(26)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("\n"
                                 "border: 4px solid;\n"
                                 "border-color: rgb(72, 57, 33);\n"
                                 "\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.482587, y1:1, x2:0.512, y2:0, stop:0 rgba(176, 128, 60, 255), stop:1 rgba(221, 162, 91, 255));\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(240, 6, 346, 583))
        self.groupBox.setStyleSheet("border: 4px solid;\n"
                                    "border-color: rgb(72, 57, 33);\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(184, 137, 71);\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.592, y1:1, x2:0.532, y2:0, stop:0.039801 rgba(214, 137, 68, 255), stop:0.512438 rgba(201, 134, 74, 251), stop:1 rgba(235, 179, 101, 255));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.name = QtWidgets.QLabel(self.groupBox)
        self.name.setGeometry(QtCore.QRect(15, 18, 301, 112))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.name.setMouseTracking(True)
        self.name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name.setStyleSheet("border: 0px;\n"
                                "background-color: rgb(255, 255, 255, 0);")
        self.name.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.name.setTextFormat(QtCore.Qt.AutoText)
        self.name.setScaledContents(True)
        self.name.setWordWrap(True)
        self.name.setIndent(0)
        self.name.setOpenExternalLinks(False)
        self.name.setObjectName("name")
        self.degree_of_roasting = QtWidgets.QLabel(self.groupBox)
        self.degree_of_roasting.setGeometry(QtCore.QRect(15, 129, 316, 112))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.degree_of_roasting.setFont(font)
        self.degree_of_roasting.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.degree_of_roasting.setMouseTracking(True)
        self.degree_of_roasting.setFocusPolicy(QtCore.Qt.NoFocus)
        self.degree_of_roasting.setStyleSheet("border: 0px;\n"
                                              "background-color: rgb(255, 255, 255, 0);")
        self.degree_of_roasting.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.degree_of_roasting.setTextFormat(QtCore.Qt.AutoText)
        self.degree_of_roasting.setScaledContents(True)
        self.degree_of_roasting.setWordWrap(True)
        self.degree_of_roasting.setIndent(0)
        self.degree_of_roasting.setOpenExternalLinks(False)
        self.degree_of_roasting.setObjectName("degree_of_roasting")
        self.shredded = QtWidgets.QLabel(self.groupBox)
        self.shredded.setGeometry(QtCore.QRect(15, 246, 316, 112))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.shredded.setFont(font)
        self.shredded.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.shredded.setMouseTracking(True)
        self.shredded.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shredded.setStyleSheet("border: 0px;\n"
                                    "background-color: rgb(255, 255, 255, 0);")
        self.shredded.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.shredded.setTextFormat(QtCore.Qt.AutoText)
        self.shredded.setScaledContents(True)
        self.shredded.setWordWrap(True)
        self.shredded.setIndent(0)
        self.shredded.setOpenExternalLinks(False)
        self.shredded.setObjectName("shredded")
        self.taste = QtWidgets.QLabel(self.groupBox)
        self.taste.setGeometry(QtCore.QRect(15, 354, 316, 112))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.taste.setFont(font)
        self.taste.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.taste.setMouseTracking(True)
        self.taste.setFocusPolicy(QtCore.Qt.NoFocus)
        self.taste.setStyleSheet("border: 0px;\n"
                                 "background-color: rgb(255, 255, 255, 0);")
        self.taste.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.taste.setTextFormat(QtCore.Qt.AutoText)
        self.taste.setScaledContents(True)
        self.taste.setWordWrap(True)
        self.taste.setIndent(0)
        self.taste.setOpenExternalLinks(False)
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QLabel(self.groupBox)
        self.price.setGeometry(QtCore.QRect(15, 456, 136, 112))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.price.setFont(font)
        self.price.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.price.setMouseTracking(True)
        self.price.setFocusPolicy(QtCore.Qt.NoFocus)
        self.price.setStyleSheet("border: 0px;\n"
                                 "background-color: rgb(255, 255, 255, 0);")
        self.price.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.price.setTextFormat(QtCore.Qt.AutoText)
        self.price.setScaledContents(True)
        self.price.setWordWrap(True)
        self.price.setIndent(0)
        self.price.setOpenExternalLinks(False)
        self.price.setObjectName("price")
        self.package_volume_grams = QtWidgets.QLabel(self.groupBox)
        self.package_volume_grams.setGeometry(QtCore.QRect(165, 459, 166, 112))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.package_volume_grams.setFont(font)
        self.package_volume_grams.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.package_volume_grams.setMouseTracking(True)
        self.package_volume_grams.setFocusPolicy(QtCore.Qt.NoFocus)
        self.package_volume_grams.setStyleSheet("border: 0px;\n"
                                                "background-color: rgb(255, 255, 255, 0);")
        self.package_volume_grams.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.package_volume_grams.setTextFormat(QtCore.Qt.AutoText)
        self.package_volume_grams.setScaledContents(True)
        self.package_volume_grams.setWordWrap(True)
        self.package_volume_grams.setIndent(0)
        self.package_volume_grams.setOpenExternalLinks(False)
        self.package_volume_grams.setObjectName("package_volume_grams")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(464, 606, 121, 40))
        self.clear_btn.setStyleSheet(".QPushButton{border-radius: 20}")
        self.clear_btn.setObjectName("clear_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(240, 606, 121, 40))
        self.add_btn.setStyleSheet(".QPushButton{border-radius: 20}")
        self.add_btn.setObjectName("add_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(375, 606, 76, 40))
        self.update_btn.setStyleSheet(".QPushButton{border-radius: 20}")
        self.update_btn.setObjectName("update_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Название сорта:"))
        self.degree_of_roasting.setText(_translate("MainWindow", "Степень обжарки:"))
        self.shredded.setText(_translate("MainWindow", "Вид:"))
        self.taste.setText(_translate("MainWindow", "Описание вкуса:"))
        self.price.setText(_translate("MainWindow", "Цена:"))
        self.package_volume_grams.setText(_translate("MainWindow", "Объем упаковки:"))
        self.clear_btn.setText(_translate("MainWindow", "Скрыть"))
        self.add_btn.setText(_translate("MainWindow", "Добавить сорт"))
        self.update_btn.setText(_translate("MainWindow", "Обновить"))

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
        # uic.loadUi('addEditCoffeeForm.ui', self)

        self.setupUi(self)

        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()

        # self.degres_of_roasting = {'Слабая': 1, 'Средняя': 2, 'Сильная': 3}

        self.add_sort_btn.clicked.connect(self.add_sort)
        self.cancel_btn.clicked.connect(self.hide)

        self.con.commit()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 474)
        Form.setStyleSheet("\n"
                           "border: 4px solid;\n"
                           "border-color: rgb(72, 57, 33);\n"
                           "\n"
                           "background-color: qlineargradient(spread:pad, x1:0.482587, y1:1, x2:0.512, y2:0, stop:0 rgba(176, 128, 60, 255), stop:1 rgba(221, 162, 91, 255));\n"
                           "\n"
                           "")
        self.add_sort_btn = QtWidgets.QPushButton(Form)
        self.add_sort_btn.setGeometry(QtCore.QRect(255, 414, 143, 45))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.add_sort_btn.setFont(font)
        self.add_sort_btn.setStyleSheet(".QPushButton{border-radius: 20}")
        self.add_sort_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.add_sort_btn.setAutoDefault(False)
        self.add_sort_btn.setObjectName("add_sort_btn")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(15, 15, 526, 373))
        self.groupBox.setStyleSheet("border: 4px solid;\n"
                                    "border-color: rgb(72, 57, 33);\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(184, 137, 71);\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.592, y1:1, x2:0.532, y2:0, stop:0.039801 rgba(214, 137, 68, 255), stop:0.512438 rgba(201, 134, 74, 251), stop:1 rgba(235, 179, 101, 255));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(15, 27, 271, 49))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setMouseTracking(True)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setStyleSheet("border: 0px;\n"
                                   "background-color: rgb(255, 255, 255, 0);")
        self.label_2.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(0)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(15, 63, 286, 76))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setMouseTracking(True)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setStyleSheet("border: 0px;\n"
                                 "background-color: rgb(255, 255, 255, 0);")
        self.label.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(15, 135, 316, 55))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setMouseTracking(True)
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setStyleSheet("border: 0px;\n"
                                   "background-color: rgb(255, 255, 255, 0);")
        self.label_3.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(0)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(15, 180, 316, 79))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_4.setMouseTracking(True)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setStyleSheet("border: 0px;\n"
                                   "background-color: rgb(255, 255, 255, 0);")
        self.label_4.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setIndent(0)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(15, 252, 136, 49))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_5.setMouseTracking(True)
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setStyleSheet("border: 0px;\n"
                                   "background-color: rgb(255, 255, 255, 0);")
        self.label_5.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setIndent(0)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(15, 297, 286, 82))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_6.setMouseTracking(True)
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_6.setStyleSheet("border: 0px;\n"
                                   "background-color: rgb(255, 255, 255, 0);")
        self.label_6.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(True)
        self.label_6.setIndent(0)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setObjectName("label_6")
        self.degree_of_roasting = QtWidgets.QLineEdit(self.groupBox)
        self.degree_of_roasting.setGeometry(QtCore.QRect(300, 96, 211, 28))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.degree_of_roasting.setFont(font)
        self.degree_of_roasting.setStyleSheet("border: 2px solid;\n"
                                              "border-color: rgb(72, 57, 33);\n"
                                              "border-radius: 4px;\n"
                                              "background-color: rgb(255, 255, 255, 0);")
        self.degree_of_roasting.setObjectName("degree_of_roasting")
        self.shredded = QtWidgets.QLineEdit(self.groupBox)
        self.shredded.setGeometry(QtCore.QRect(300, 147, 211, 28))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.shredded.setFont(font)
        self.shredded.setStyleSheet("border: 2px solid;\n"
                                    "border-color: rgb(72, 57, 33);\n"
                                    "border-radius: 4px;\n"
                                    "background-color: rgb(255, 255, 255, 0);")
        self.shredded.setObjectName("shredded")
        self.taste = QtWidgets.QLineEdit(self.groupBox)
        self.taste.setGeometry(QtCore.QRect(300, 207, 211, 28))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.taste.setFont(font)
        self.taste.setStyleSheet("border: 2px solid;\n"
                                 "border-color: rgb(72, 57, 33);\n"
                                 "border-radius: 4px;\n"
                                 "background-color: rgb(255, 255, 255, 0);")
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QLineEdit(self.groupBox)
        self.price.setGeometry(QtCore.QRect(300, 267, 211, 28))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.price.setFont(font)
        self.price.setStyleSheet("border: 2px solid;\n"
                                 "border-color: rgb(72, 57, 33);\n"
                                 "border-radius: 4px;\n"
                                 "background-color: rgb(255, 255, 255, 0);")
        self.price.setObjectName("price")
        self.package_volume_grams = QtWidgets.QLineEdit(self.groupBox)
        self.package_volume_grams.setGeometry(QtCore.QRect(300, 327, 211, 28))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.package_volume_grams.setFont(font)
        self.package_volume_grams.setStyleSheet("border: 2px solid;\n"
                                                "border-color: rgb(72, 57, 33);\n"
                                                "border-radius: 4px;\n"
                                                "background-color: rgb(255, 255, 255, 0);")
        self.package_volume_grams.setObjectName("package_volume_grams")
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(300, 39, 211, 28))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.name.setFont(font)
        self.name.setStyleSheet("border: 2px solid;\n"
                                "border-color: rgb(72, 57, 33);\n"
                                "border-radius: 4px;\n"
                                "background-color: rgb(255, 255, 255, 0);")
        self.name.setObjectName("name")
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(405, 414, 143, 45))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(".QPushButton{border-radius: 20}")
        self.cancel_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_sort_btn.setText(_translate("Form", "Добавить сорт"))
        self.label_2.setText(_translate("Form", "Название сорта:"))
        self.label.setText(_translate("Form", "Степень обжарки(1, 2 или 3): "))
        self.label_3.setText(_translate("Form", "Вид(молотый/зерновой):"))
        self.label_4.setText(_translate("Form", "Описание вкуса:"))
        self.label_5.setText(_translate("Form", "Цена:"))
        self.label_6.setText(_translate("Form", "Объем упаковки:"))
        self.cancel_btn.setText(_translate("Form", "Отмена"))

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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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

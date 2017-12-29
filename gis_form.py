# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gis.ui'
#
# Created: Sun Oct 29 11:20:02 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Windows(object):
    def setupUi(self, Windows):
        Windows.setObjectName(_fromUtf8("Windows"))
        Windows.setEnabled(True)
        Windows.resize(674, 375)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Windows.sizePolicy().hasHeightForWidth())
        Windows.setSizePolicy(sizePolicy)
        Windows.setMinimumSize(QtCore.QSize(0, 0))
        Windows.setSizeIncrement(QtCore.QSize(0, 0))
        Windows.setBaseSize(QtCore.QSize(0, 0))
        Windows.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/image2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Windows.setWindowIcon(icon)
        self.longutide = QtGui.QLineEdit(Windows)
        self.longutide.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.longutide.setObjectName(_fromUtf8("longutide"))
        self.label = QtGui.QLabel(Windows)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Windows)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.latitude = QtGui.QLineEdit(Windows)
        self.latitude.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.latitude.setObjectName(_fromUtf8("latitude"))
        self.label_3 = QtGui.QLabel(Windows)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.speed = QtGui.QLineEdit(Windows)
        self.speed.setGeometry(QtCore.QRect(10, 210, 71, 21))
        self.speed.setObjectName(_fromUtf8("speed"))
        self.start = QtGui.QPushButton(Windows)
        self.start.setGeometry(QtCore.QRect(590, 240, 75, 31))
        self.start.setObjectName(_fromUtf8("start"))
        self.end = QtGui.QPushButton(Windows)
        self.end.setGeometry(QtCore.QRect(590, 290, 75, 31))
        self.end.setObjectName(_fromUtf8("end"))
        self.serial = QtGui.QComboBox(Windows)
        self.serial.setGeometry(QtCore.QRect(590, 30, 69, 22))
        self.serial.setObjectName(_fromUtf8("serial"))
        self.label_4 = QtGui.QLabel(Windows)
        self.label_4.setGeometry(QtCore.QRect(590, 10, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox = QtGui.QComboBox(Windows)
        self.comboBox.setGeometry(QtCore.QRect(590, 110, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, _fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(Windows)
        self.label_5.setGeometry(QtCore.QRect(590, 90, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.interval = QtGui.QLineEdit(Windows)
        self.interval.setGeometry(QtCore.QRect(10, 310, 71, 20))
        self.interval.setObjectName(_fromUtf8("interval"))
        self.label_6 = QtGui.QLabel(Windows)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.about = QtGui.QPushButton(Windows)
        self.about.setGeometry(QtCore.QRect(600, 340, 61, 21))
        self.about.setObjectName(_fromUtf8("about"))
        self.display = QtGui.QTextEdit(Windows)
        self.display.setGeometry(QtCore.QRect(110, 60, 471, 271))
        self.display.setObjectName(_fromUtf8("display"))
        self.clean = QtGui.QPushButton(Windows)
        self.clean.setGeometry(QtCore.QRect(590, 190, 75, 31))
        self.clean.setObjectName(_fromUtf8("clean"))

        self.retranslateUi(Windows)
        QtCore.QMetaObject.connectSlotsByName(Windows)

    def retranslateUi(self, Windows):
        Windows.setWindowTitle(_translate("Windows", "0183生成器", None))
        self.longutide.setText(_translate("Windows", "11325.9527", None))
        self.label.setText(_translate("Windows", "经度(dddmm.mmmm)", None))
        self.label_2.setText(_translate("Windows", "纬度(ddmm.mmmm)", None))
        self.latitude.setText(_translate("Windows", "2308.9503", None))
        self.label_3.setText(_translate("Windows", "速度(000.0-999.9)", None))
        self.speed.setText(_translate("Windows", "999.9", None))
        self.start.setText(_translate("Windows", "开始", None))
        self.end.setText(_translate("Windows", "结束", None))
        self.label_4.setText(_translate("Windows", "串口", None))
        self.comboBox.setItemText(1, _translate("Windows", "9600", None))
        self.comboBox.setItemText(2, _translate("Windows", "38400", None))
        self.comboBox.setItemText(3, _translate("Windows", "115200", None))
        self.label_5.setText(_translate("Windows", "波特率", None))
        self.interval.setText(_translate("Windows", "1", None))
        self.label_6.setText(_translate("Windows", "发送时间间隔(s)", None))
        self.about.setText(_translate("Windows", "关于", None))
        self.clean.setText(_translate("Windows", "清屏", None))

import titleico_rc

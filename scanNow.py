# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanNow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scanNow(object):
    def setupUi(self, scanNow):
        scanNow.setObjectName("scanNow")
        scanNow.resize(300, 70)
        scanNow.setMinimumSize(QtCore.QSize(300, 70))
        scanNow.setMaximumSize(QtCore.QSize(300, 70))
        self.verticalLayout = QtWidgets.QVBoxLayout(scanNow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.eventData = QtWidgets.QLabel(scanNow)
        self.eventData.setAlignment(QtCore.Qt.AlignCenter)
        self.eventData.setObjectName("eventData")
        self.verticalLayout.addWidget(self.eventData)
        self.scanLine = QtWidgets.QLineEdit(scanNow)
        self.scanLine.setObjectName("scanLine")
        self.verticalLayout.addWidget(self.scanLine)

        self.retranslateUi(scanNow)
        QtCore.QMetaObject.connectSlotsByName(scanNow)

    def retranslateUi(self, scanNow):
        _translate = QtCore.QCoreApplication.translate
        scanNow.setWindowTitle(_translate("scanNow", "Scan Now"))
        self.eventData.setText(_translate("scanNow", "TextLabel"))

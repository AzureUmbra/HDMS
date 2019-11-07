# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventCheckInOut.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventCheckInOut(object):
    def setupUi(self, EventCheckInOut):
        EventCheckInOut.setObjectName("EventCheckInOut")
        EventCheckInOut.resize(550, 141)
        EventCheckInOut.setMinimumSize(QtCore.QSize(550, 141))
        EventCheckInOut.setMaximumSize(QtCore.QSize(550, 141))
        self.verticalLayout = QtWidgets.QVBoxLayout(EventCheckInOut)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(EventCheckInOut)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(EventCheckInOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(EventCheckInOut)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(EventCheckInOut)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filterEventList = QtWidgets.QPushButton(EventCheckInOut)
        self.filterEventList.setObjectName("filterEventList")
        self.horizontalLayout_2.addWidget(self.filterEventList)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(EventCheckInOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_2.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_2.setSizePolicy(sizePolicy)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(EventCheckInOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(EventCheckInOut)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(EventCheckInOut)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.pushButton_2 = QtWidgets.QPushButton(EventCheckInOut)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(EventCheckInOut)
        QtCore.QMetaObject.connectSlotsByName(EventCheckInOut)

    def retranslateUi(self, EventCheckInOut):
        _translate = QtCore.QCoreApplication.translate
        EventCheckInOut.setWindowTitle(_translate("EventCheckInOut", "Event Check-In/Out"))
        self.label.setText(_translate("EventCheckInOut", "Select Event: "))
        self.pushButton.setText(_translate("EventCheckInOut", "Create New Event"))
        self.filterEventList.setText(_translate("EventCheckInOut", "Filter Event List"))
        self.checkBox.setText(_translate("EventCheckInOut", "Quick Scanning"))
        self.pushButton_2.setText(_translate("EventCheckInOut", "Begin Check-In/Out"))

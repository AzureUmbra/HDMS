# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createEvent.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateEvent(object):
    def setupUi(self, CreateEvent):
        CreateEvent.setObjectName("CreateEvent")
        CreateEvent.resize(500, 127)
        CreateEvent.setMinimumSize(QtCore.QSize(500, 127))
        CreateEvent.setMaximumSize(QtCore.QSize(500, 127))
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateEvent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CreateEvent)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.eventName = QtWidgets.QLineEdit(CreateEvent)
        self.eventName.setObjectName("eventName")
        self.horizontalLayout.addWidget(self.eventName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(CreateEvent)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.startTime = QtWidgets.QDateTimeEdit(CreateEvent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTime.sizePolicy().hasHeightForWidth())
        self.startTime.setSizePolicy(sizePolicy)
        self.startTime.setCalendarPopup(True)
        self.startTime.setObjectName("startTime")
        self.horizontalLayout_4.addWidget(self.startTime)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(CreateEvent)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.endTime = QtWidgets.QDateTimeEdit(CreateEvent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endTime.sizePolicy().hasHeightForWidth())
        self.endTime.setSizePolicy(sizePolicy)
        self.endTime.setCalendarPopup(True)
        self.endTime.setObjectName("endTime")
        self.horizontalLayout_2.addWidget(self.endTime)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancel = QtWidgets.QPushButton(CreateEvent)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_3.addWidget(self.cancel)
        self.confirm = QtWidgets.QPushButton(CreateEvent)
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_3.addWidget(self.confirm)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(CreateEvent)
        QtCore.QMetaObject.connectSlotsByName(CreateEvent)

    def retranslateUi(self, CreateEvent):
        _translate = QtCore.QCoreApplication.translate
        CreateEvent.setWindowTitle(_translate("CreateEvent", "Create Event"))
        self.label.setText(_translate("CreateEvent", "Event Name: "))
        self.label_2.setText(_translate("CreateEvent", "Start Date and Time: "))
        self.label_3.setText(_translate("CreateEvent", "End Date and Time:   "))
        self.cancel.setText(_translate("CreateEvent", "Cancel"))
        self.confirm.setText(_translate("CreateEvent", "Confirm"))

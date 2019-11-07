# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hsuDataMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HsuDataManagementSystem(object):
    def setupUi(self, HsuDataManagementSystem):
        HsuDataManagementSystem.setObjectName("HsuDataManagementSystem")
        HsuDataManagementSystem.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        HsuDataManagementSystem.setFont(font)
        self.centralwidget = QtWidgets.QWidget(HsuDataManagementSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.results = QtWidgets.QTextBrowser(self.centralwidget)
        self.results.setMinimumSize(QtCore.QSize(0, 0))
        self.results.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.results.setObjectName("results")
        self.horizontalLayout_3.addWidget(self.results)
        HsuDataManagementSystem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HsuDataManagementSystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuScanning = QtWidgets.QMenu(self.menubar)
        self.menuScanning.setObjectName("menuScanning")
        self.menuQueries = QtWidgets.QMenu(self.menubar)
        self.menuQueries.setObjectName("menuQueries")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        HsuDataManagementSystem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HsuDataManagementSystem)
        self.statusbar.setObjectName("statusbar")
        HsuDataManagementSystem.setStatusBar(self.statusbar)
        self.checkInOutToggle = QtWidgets.QAction(HsuDataManagementSystem)
        self.checkInOutToggle.setCheckable(True)
        self.checkInOutToggle.setChecked(True)
        self.checkInOutToggle.setObjectName("checkInOutToggle")
        self.actionPersonnel = QtWidgets.QAction(HsuDataManagementSystem)
        self.actionPersonnel.setObjectName("actionPersonnel")
        self.actionEquipment = QtWidgets.QAction(HsuDataManagementSystem)
        self.actionEquipment.setObjectName("actionEquipment")
        self.actionMember = QtWidgets.QAction(HsuDataManagementSystem)
        self.actionMember.setObjectName("actionMember")
        self.menuScanning.addAction(self.actionPersonnel)
        self.menuScanning.addAction(self.actionEquipment)
        self.menuEdit.addAction(self.actionMember)
        self.menubar.addAction(self.menuScanning.menuAction())
        self.menubar.addAction(self.menuQueries.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(HsuDataManagementSystem)
        QtCore.QMetaObject.connectSlotsByName(HsuDataManagementSystem)

    def retranslateUi(self, HsuDataManagementSystem):
        _translate = QtCore.QCoreApplication.translate
        HsuDataManagementSystem.setWindowTitle(_translate("HsuDataManagementSystem", "Hsu Data Management System"))
        self.menuScanning.setTitle(_translate("HsuDataManagementSystem", "Scanning"))
        self.menuQueries.setTitle(_translate("HsuDataManagementSystem", "Queries"))
        self.menuReports.setTitle(_translate("HsuDataManagementSystem", "Reports"))
        self.menuEdit.setTitle(_translate("HsuDataManagementSystem", "Edit"))
        self.checkInOutToggle.setText(_translate("HsuDataManagementSystem", "Check-In/Out"))
        self.actionPersonnel.setText(_translate("HsuDataManagementSystem", "Event Sign-In/Out"))
        self.actionEquipment.setText(_translate("HsuDataManagementSystem", "Equipment Check-In/Out"))
        self.actionMember.setText(_translate("HsuDataManagementSystem", "Member"))

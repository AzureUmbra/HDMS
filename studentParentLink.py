# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentParentLink.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentParentLink(object):
    def setupUi(self, StudentParentLink):
        StudentParentLink.setObjectName("StudentParentLink")
        StudentParentLink.resize(400, 128)
        StudentParentLink.setMinimumSize(QtCore.QSize(400, 128))
        StudentParentLink.setMaximumSize(QtCore.QSize(400, 128))
        self.verticalLayout = QtWidgets.QVBoxLayout(StudentParentLink)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(StudentParentLink)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.relationship = QtWidgets.QLineEdit(StudentParentLink)
        self.relationship.setObjectName("relationship")
        self.horizontalLayout.addWidget(self.relationship)
        self.canCollect = QtWidgets.QCheckBox(StudentParentLink)
        self.canCollect.setObjectName("canCollect")
        self.horizontalLayout.addWidget(self.canCollect)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(StudentParentLink)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(StudentParentLink)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(StudentParentLink)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(StudentParentLink)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.removeStudent = QtWidgets.QCheckBox(StudentParentLink)
        self.removeStudent.setObjectName("removeStudent")
        self.verticalLayout.addWidget(self.removeStudent)

        self.retranslateUi(StudentParentLink)
        QtCore.QMetaObject.connectSlotsByName(StudentParentLink)

    def retranslateUi(self, StudentParentLink):
        _translate = QtCore.QCoreApplication.translate
        StudentParentLink.setWindowTitle(_translate("StudentParentLink", "Link Student to Parent"))
        self.label.setText(_translate("StudentParentLink", "Relationship: "))
        self.canCollect.setText(_translate("StudentParentLink", "Can Collect Student"))
        self.label_2.setText(_translate("StudentParentLink", "Scan Student Barcode"))
        self.removeStudent.setText(_translate("StudentParentLink", "Check to Remove Student from Parent"))

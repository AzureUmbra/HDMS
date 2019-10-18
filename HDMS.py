from hsuDataMain import Ui_HsuDataManagementSystem
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import sys

import mysql.connector
from mysql.connector import Error

class HsuDataManagementSystem:
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.main = Ui_HsuDataManagementSystem()
        self.main.setupUi(self.mainWindow)
        self.mainWindow.closeEvent = self.close

        self.mainWindow.show()

        try:
            self.connection = mysql.connector.connect(host='127.0.0.1',database='hsutracker',user='root',password='')
            #self.connection.

        except Error as e:
            print("Error while connecting to MySQL", e)

        self.main.checkInOutLine.returnPressed.connect(self.test)

        self.main.checkInLed.setProperty('flipper','true')
        self.main.checkOutLed.setProperty('flipper', 'true')
        self.mainWindow.setStyleSheet('QLabel[flipper=true]:disabled{color:red;} QLabel[flipper=true]:!disabled{color:green;}')
        self.main.checkInLed.setStyle(self.main.checkInLed.style())


    def close(self, event):
        msg = "Are you sure you want to exit?"
        reply = QtWidgets.QMessageBox.question(self.mainWindow, "Exit?", msg)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def test(self):
        #self.main.textBrowser.append(self.main.checkInOutLine.text())
        try:
            query = 'SELECT * FROM members WHERE idBarcode="{}"'.format(self.main.checkInOutLine.text())
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchone()
            resultString = ''
            for i in result.keys():
                resultString += '{}: {}\n'.format(i,result[i])
            self.main.textBrowser.setText(resultString)
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        self.main.checkInOutLine.clear()







if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    gui = HsuDataManagementSystem()
    sys.exit(app.exec_())
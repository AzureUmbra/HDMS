from hsuDataMain import Ui_HsuDataManagementSystem
from PyQt5 import QtCore, QtGui, QtWidgets
from windows import createEvent, eventCheckInOut, scanNow
from datetime import datetime
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

        try:
            self.connection = mysql.connector.connect(host='127.0.0.1',database='hsutracker',user='root',password='')
            #self.connection.
        except Error as e:
            print("Error while connecting to MySQL", e)

        self.createEvent = createEvent(self.connection)
        self.selectEvent = eventCheckInOut(self.connection)
        self.scanNow = scanNow(self.connection)

        self.main.actionPersonnel.triggered.connect(self.checkIn)
        self.selectEvent.widget.pushButton.clicked.connect(self.newEvent)
        self.selectEvent.widget.pushButton_2.clicked.connect(self.beginScanningEvent)
        self.createEvent.widget.confirm.clicked.connect(self.createNewEvent)
        self.scanNow.widget.scanLine.returnPressed.connect(self.scanIn)

        self.currentEvent = ''
        self.quickScan = False

        self.mainWindow.show()

    def printResults(self,msg):
        self.main.results.append(str(datetime.now().strftime("%H:%M:%S")) + '- ' + str(msg))

    def newEvent(self):
        self.createEvent.window.show()

    def checkIn(self):
        self.selectEvent.window.show()
        self.selectEvent.open()

    def createNewEvent(self):
        self.createEvent.confirm()
        self.selectEvent.open()

    def beginScanningEvent(self):
        id = self.selectEvent.widget.comboBox.currentText().split('-')[0]
        query = 'SELECT * FROM event WHERE id={}'.format(id)
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        event = cursor.fetchone()
        cursor.close()
        self.currentEvent = event['id']
        self.scanNow.window.show()
        self.scanNow.open(event['name'])
        self.quickScan = self.selectEvent.widget.checkBox.isChecked()
        self.selectEvent.window.hide()

    def scanIn(self):
        user = self.scanNow.widget.scanLine.text()
        self.scanNow.widget.scanLine.clear()
        query = 'SELECT * FROM members m INNER JOIN entity e ON e.id = m.id WHERE e.idBarcode={}'.format(user)
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        member = cursor.fetchone()
        cursor.close()
        if member == None:
            print('no individual exists')
        else:
            query = 'SELECT direction FROM joineventmember WHERE idMember={} ORDER BY datetime DESC LIMIT 1'.format(member['id'])
            cursor = self.connection.cursor()
            cursor.execute(query)
            last = cursor.fetchone()
            cursor.close()
            direction = 1 if last == None or last == (0,) else 0
            query = 'INSERT INTO joineventmember (idMember,idEvent,direction,datetime) VALUES (%s,%s,%s,%s)'
            values = (member['id'], self.currentEvent, direction, datetime.now())
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            msg = "{} {} has been successfully signed-{}".format(member['fName'],member['lName'],'in' if direction == 1 else 'out')
            if not self.quickScan:
                QtWidgets.QMessageBox.information(self.scanNow.window,"Success!",msg)
            self.printResults(msg)



    def close(self, event):
        msg = "Are you sure you want to exit?"
        reply = QtWidgets.QMessageBox.question(self.mainWindow, "Exit?", msg)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    gui = HsuDataManagementSystem()
    sys.exit(app.exec_())
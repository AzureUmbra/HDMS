from PyQt5 import QtCore, QtGui, QtWidgets
from createEvent import Ui_CreateEvent
from eventCheckInOut import Ui_EventCheckInOut
from scanNow import Ui_scanNow

class createEvent:
    def __init__(self,connection):
        self.connection = connection
        self.window = QtWidgets.QWidget()
        self.widget = Ui_CreateEvent()
        self.widget.setupUi(self.window)
        self.widget.closeEvent = self.close

        # Connect "Confirm" in Parent
        self.widget.cancel.clicked.connect(self.cancel)

    def cancel(self):
        self.widget.endTime.clear()
        self.widget.startTime.clear()
        self.widget.eventName.clear()
        self.window.hide()

    def confirm(self):
        if self.widget.eventName != '' and self.widget.endTime.dateTime() > self.widget.startTime.dateTime():
            query = 'INSERT INTO event (name,startTime,endTime) VALUES (%s,%s,%s)'
            values = (self.widget.eventName.text(),str(self.widget.startTime.dateTime().toPyDateTime()),str(self.widget.endTime.dateTime().toPyDateTime()))
            cursor = self.connection.cursor()
            cursor.execute(query,values)
            self.connection.commit()
            cursor.close()
            self.cancel()
        else:
            print('bad option')

    def close(self,event):
        self.window.hide()
        event.ignore()


class eventCheckInOut:
    def __init__(self,connection):
        self.connection = connection
        self.window = QtWidgets.QWidget()
        self.widget = Ui_EventCheckInOut()
        self.widget.setupUi(self.window)
        self.widget.closeEvent = self.close

        self.eventList = []

        self.widget.filterEventList.clicked.connect(self.filter)
        # Create New Event created in Main
        # Begin created in Main

    def open(self):
        self.widget.checkBox.setChecked(False)
        self.widget.comboBox.clear()
        query = 'SELECT * FROM event'
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        self.eventList = cursor.fetchall()
        cursor.close()
        self.widget.comboBox.addItems([str(i['id']) + '- ' + str(i['name']) + '@ ' + str(i['startTime']) for i in self.eventList])

    def filter(self):
        self.widget.comboBox.clear()
        self.widget.comboBox.addItems([str(i['id']) + '- ' + str(i['name']) + '@ ' + str(i['startTime']) for i in self.eventList if i['startTime'] >= self.widget.dateTimeEdit_2.dateTime() and i['endTime'] <= self.widget.dateTimeEdit.dateTime()])

    def close(self, event):
        self.window.hide()
        event.ignore()


class scanNow:
    def __init__(self,connection):
        self.connection = connection
        self.window = QtWidgets.QWidget()
        self.widget = Ui_scanNow()
        self.widget.setupUi(self.window)
        self.widget.closeEvent = self.close

    def open(self,text):
        self.widget.eventData.setText('Check-In/Out is now open for {}'.format(text))
        self.widget.scanLine.setFocus()

    def close(self, event):
        self.window.hide()
        event.ignore()


# class eventCheckInOut:
#     def __init__(self,connection):
#         self.connection = connection
#         self.window = QtWidgets.QWidget()
#         self.widget = Ui_EventCheckInOut()
#         self.widget.setupUi(self.window)
#         self.widget.closeEvent = self.close
#
#     def close(self, event):
#         self.window.hide()
#         event.ignore()
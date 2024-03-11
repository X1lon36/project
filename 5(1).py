from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from sys import exit, argv
 
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 263)
        font = QtGui.QFont()
        font.setPointSize(10)
 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ddmmyyyy = QtWidgets.QDateEdit(self.centralwidget)
        self.ddmmyyyy.setGeometry(QtCore.QRect(10, 110, 110, 22))
        self.ddmmyyyy.setObjectName("ddmyyyy")
        self.time = QtWidgets.QTimeEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(130, 110, 91, 22))
        self.time.setObjectName("time")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 30, 211, 41))
        self.name.setFont(font)
        self.name.setText("")
        self.name.setObjectName("name")
        self.getout = QtWidgets.QPushButton(self.centralwidget)
        self.getout.setGeometry(QtCore.QRect(50, 150, 141, 41))
        self.getout.setObjectName("getout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(250, 30, 221, 211))
        self.listWidget.setObjectName("listWidget")
        self.event = QtWidgets.QLabel(self.centralwidget)
        self.event.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.event.setFont(font)
        self.event.setAlignment(QtCore.Qt.AlignCenter)
        self.event.setObjectName("event")
        self.data = QtWidgets.QLabel(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(10, 80, 211, 21))
        self.data.setFont(font)
        self.data.setAlignment(QtCore.Qt.AlignCenter)
        self.data.setObjectName("data")
        self.nameofevent = QtWidgets.QLabel(self.centralwidget)
        self.nameofevent.setGeometry(QtCore.QRect(250, 10, 51, 16))
        self.nameofevent.setFont(font)
        self.nameofevent.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nameofevent.setObjectName("nameofevent")
        self.dataofevent = QtWidgets.QLabel(self.centralwidget)
        self.dataofevent.setGeometry(QtCore.QRect(335, 10, 51, 16))
        self.dataofevent.setFont(font)
        self.dataofevent.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.dataofevent.setObjectName("dataofevent")
        self.timeofevent = QtWidgets.QLabel(self.centralwidget)
        self.timeofevent.setGeometry(QtCore.QRect(415, 10, 51, 16))
        self.timeofevent.setFont(font)
        self.timeofevent.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.timeofevent.setObjectName("timeofevent")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ежедневник"))
        self.getout.setText(_translate("MainWindow", "Добавить"))
        self.listWidget.setSortingEnabled(True)
        self.listWidget.sortItems()
        self.listWidget.sortItems(QtCore.Qt.DescendingOrder)
        self.event.setText(_translate("MainWindow", "Название события:"))
        self.data.setText(_translate("MainWindow", "Дата и время проведения:"))
        self.nameofevent.setText(_translate("MainWindow", "Имя:"))
        self.dataofevent.setText(_translate("MainWindow", "Дата:"))
        self.timeofevent.setText(_translate("MainWindow", "Время:"))
 
 
class Dateedit(QMainWindow, Ui_MainWindow):
 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
 
        self.k = 0
        self.d = {}
 
        self.getout.clicked.connect(self.out)
 
    def out(self):
        self.d[self.name.text()] = (self.ddmmyyyy.date(), self.time.time())
        _translate = QtCore.QCoreApplication.translate
        self.listWidget.addItem(QtWidgets.QListWidgetItem())
        item = self.listWidget.item(self.k)
        for i, j in self.d.items():
            item.setText(_translate("SecondWindow", f'{i} \t{j[0].day()}.{j[0].month()}.{j[0].year()} '
                                                    f'\tв {j[1].hour()}:{j[1].minute()}'))
        self.k += 1
 
 
if __name__ == '__main__':
    app = QApplication(argv)
    ex = Dateedit()
    ex.show()
    exit(app.exec())
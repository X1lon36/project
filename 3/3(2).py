from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(60, 70, 82, 17))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 130, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 110, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(60, 90, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 200, 71, 21))
        self.checkBox.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.checkBox.setProperty("color", QtGui.QColor(170, 0, 0))
        self.checkBox.setObjectName("checkBox")
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 220, 71, 21))
        self.checkBox_2.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 240, 71, 21))
        self.checkBox_3.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.checkBox_3.setObjectName("checkBox_3")
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 260, 71, 21))
        self.checkBox_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.checkBox_4.setObjectName("checkBox_4")
        

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 71, 41))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 71, 41))
        self.label_2.setObjectName("label_2")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        
        self.radioButton.setText(_translate("MainWindow", "0-10"))
        
        self.radioButton_2.setText(_translate("MainWindow", "30-40"))
        
        self.radioButton_3.setText(_translate("MainWindow", "20-30"))
        
        self.radioButton_4.setText(_translate("MainWindow", "10-20"))
        
        
        self.checkBox.setText(_translate("MainWindow", "red"))
        
        self.checkBox_2.setText(_translate("MainWindow", "blue"))
        
        self.checkBox_3.setText(_translate("MainWindow", "green"))
        
        self.checkBox_4.setText(_translate("MainWindow", "yellow"))
        
        
        self.label.setText(_translate("MainWindow", "Количество"))
        
        self.label_2.setText(_translate("MainWindow", "Цвет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

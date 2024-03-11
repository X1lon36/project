from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("main program")
    window.setGeometry(300, 400, 350, 350)
    
    
    main_text = QtWidgets.QLabel(window)
    main_text.setText("give your addr: ")
    main_text.move(10, 20)
    main_text.adjustSize()

    textbox = QtWidgets.QLineEdit(window)  
    textbox.move( 10 , 40 ) 
    textbox.resize( 280 , 30 )

    main_text = QtWidgets.QLabel(window)
    main_text.setText("комментарий")
    main_text.move(10, 75)
    main_text.adjustSize()

    textbox = QtWidgets.QLineEdit(window)  
    textbox.move( 10 , 100 ) 
    textbox.resize( 280 , 120 )
    textbox.adjustSize()

    main_button = QtWidgets.QPushButton(window)
    main_button.setText("отправить")              
    main_button.move(150, 180)                 
    main_button.adjustSize()                    
    main_button.clicked.connect(info)


    window.show()
    sys.exit(app.exec_())

def info():
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText("Отправлено")
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.exec_()





if __name__ == "__main__":
    application()

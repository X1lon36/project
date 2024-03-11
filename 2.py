from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()          #создание главного окна

    window.setWindowTitle("main program")       #название главного окна
    window.setGeometry(300, 250, 350, 200)      # размеры окна

    main_text = QtWidgets.QLabel(window)        #создание текста в главном окне 
    main_text.setText("hello world")            #сам текст
    main_text.move(100, 50)                     #размеры отступа от левого и верхнего края
    main_text.adjustSize()                      #расчет размеров виджета


    main_button = QtWidgets.QPushButton(window) #создание текста в главном окне 
    main_button.setText("friend!")              #название кнопки
    main_button.move(150, 100)                  #отступы от краёв
    main_button.adjustSize()                    
    main_button.clicked.connect(button1)        #присваивание кнопки то-что она будет делать


    main_button = QtWidgets.QPushButton(window)
    main_button.setText("near!")
    main_button.move(150, 125)
    main_button.adjustSize()
    main_button.clicked.connect(button2)


    window.show()
    sys.exit(app.exec_())

def button1():                                  #присваивание к какой кнопке это относится
    print("hello friend!")                      #то-что она выполняет
def button2():                                  
    print("I'm near")                           



if __name__ == "__main__":
    application()
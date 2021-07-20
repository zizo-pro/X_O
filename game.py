
from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv



FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"game.ui"))

class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button_setup()
        self.font = QFont()
        self.font.setPointSize(65)
        self.X = True
        self.O = False

    def xscore(self):
        xscre = self.x_score.text()
        new_score = int(xscre)+1
        self.x_score.setText(str(new_score))
        self.reset.show()
        
    def oscore(self):
        oscre = self.o_score.text()
        new_score = int(oscre)+1
        self.o_score.setText(str(new_score))
        self.reset.show()

    def rest(self):
        self.button_1.setText("")
        self.button_2.setText("")
        self.button_3.setText("")
        self.button_4.setText("")
        self.button_5.setText("")
        self.button_6.setText("")
        self.button_7.setText("")
        self.button_8.setText("")
        self.button_9.setText("")

        self.button_1.setEnabled(True)
        self.button_2.setEnabled(True)
        self.button_3.setEnabled(True)
        self.button_4.setEnabled(True)
        self.button_5.setEnabled(True)
        self.button_6.setEnabled(True)
        self.button_7.setEnabled(True)
        self.button_8.setEnabled(True)
        self.button_9.setEnabled(True)

    def button_setup(self):
        self.button_1.clicked.connect(self.button1)
        self.button_2.clicked.connect(self.button2)
        self.button_3.clicked.connect(self.button3)
        self.button_4.clicked.connect(self.button4)
        self.button_5.clicked.connect(self.button5)
        self.button_6.clicked.connect(self.button6)
        self.button_7.clicked.connect(self.button7)
        self.button_8.clicked.connect(self.button8)
        self.button_9.clicked.connect(self.button9)
        self.button_1.clicked.connect(self.checkwin)
        self.button_2.clicked.connect(self.checkwin)
        self.button_3.clicked.connect(self.checkwin)
        self.button_4.clicked.connect(self.checkwin)
        self.button_5.clicked.connect(self.checkwin)
        self.button_6.clicked.connect(self.checkwin)
        self.button_7.clicked.connect(self.checkwin)
        self.button_8.clicked.connect(self.checkwin)
        self.button_9.clicked.connect(self.checkwin)
        self.reset.clicked.connect(self.rest)

    def button1 (self):
        if self.X == True:
            self.button_1.setFont(self.font)
            self.button_1.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_1.setFont(self.font)
            self.button_1.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_1.setFont(self.font)
            self.button_1.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_1.setFont(self.font)
            self.button_1.setText("O")
            self.X = True
            self.O = False
        self.button_1.setEnabled(False)

    def button2 (self):
        if self.X == True:
            self.button_2.setFont(self.font)
            self.button_2.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_2.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_2.setFont(self.font)
            self.button_2.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_2.setText("O")
            self.X = True
            self.O = False
        self.button_2.setEnabled(False)

    def button3 (self):
        if self.X == True:
            self.button_3.setFont(self.font)
            self.button_3.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_3.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_3.setFont(self.font)
            self.button_3.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_3.setText("O")
            self.X = True
            self.O = False
        self.button_3.setEnabled(False)

    def button4 (self):
        if self.X == True:
            self.button_4.setFont(self.font)
            self.button_4.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_4.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_4.setFont(self.font)
            self.button_4.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_4.setText("O")
            self.X = True
            self.O = False
        self.button_4.setEnabled(False)

    def button5 (self):
        if self.X == True:
            self.button_5.setFont(self.font)
            self.button_5.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_5.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_5.setFont(self.font)
            self.button_5.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_5.setText("O")
            self.X = True
            self.O = False
        self.button_5.setEnabled(False)

    def button6 (self):
        if self.X == True:
            self.button_6.setFont(self.font)
            self.button_6.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_6.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_6.setFont(self.font)
            self.button_6.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_6.setText("O")
            self.X = True
            self.O = False
        self.button_6.setEnabled(False)

    def button7 (self):
        if self.X == True:
            self.button_7.setFont(self.font)
            self.button_7.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_7.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_7.setFont(self.font)
            self.button_7.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_7.setText("O")
            self.X = True
            self.O = False
        self.button_7.setEnabled(False)

    def button8 (self):
        if self.X == True:
            self.button_8.setFont(self.font)
            self.button_8.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_8.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_8.setFont(self.font)
            self.button_8.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_8.setText("O")
            self.X = True
            self.O = False
        self.button_8.setEnabled(False)

    def button9 (self):
        if self.X == True:
            self.button_9.setFont(self.font)
            self.button_9.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_9.setText("X")
            self.X = False
            self.O = True
        elif self.O == True:
            self.button_9.setFont(self.font)
            self.button_9.setStyleSheet("color: rgb(0, 255, 0);")
            self.button_9.setText("O")
            self.X = True
            self.O = False
        self.button_9.setEnabled(False)

    def checkwin(self):
        if self.button_1.text() == "X" and self.button_2.text() == "X" and self.button_3.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()
        elif self.button_1.text() == "O" and self.button_2.text() == "O" and self.button_3.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_1.text() == "X" and self.button_4.text() == "X" and self.button_7.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()
        elif self.button_1.text() == "O" and self.button_4.text() == "O" and self.button_7.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_2.text() == "X" and self.button_5.text() == "X" and self.button_8.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()
        elif self.button_2.text() == "O" and self.button_5.text() == "O" and self.button_8.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_4.text() == "X" and self.button_5.text() == "X" and self.button_6.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()
        elif self.button_4.text() == "O" and self.button_5.text() == "O" and self.button_6.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_7.text() == "X" and self.button_8.text() == "X" and self.button_9.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()
        elif self.button_7.text() == "O" and self.button_8.text() == "O" and self.button_9.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_3.text() == "X" and self.button_6.text() == "X" and self.button_9.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()
        elif self.button_3.text() == "O" and self.button_6.text() == "O" and self.button_9.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_1.text() == "X" and self.button_5.text() == "X" and self.button_9.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()
        elif self.button_1.text() == "O" and self.button_5.text() == "O" and self.button_9.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_3.text() == "O" and self.button_5.text() == "O" and self.button_7.text() == "O":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.oscore()

        elif self.button_3.text() == "X" and self.button_5.text() == "X" and self.button_7.text() == "X":
    
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.xscore()

if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = mainapp()
    window.show()
    app.exec()
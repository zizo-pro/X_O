# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from io import BufferedIOBase
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(555, 555)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(170, 100, 31, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.button_1 = QtWidgets.QPushButton(Form)
        self.button_1.setGeometry(QtCore.QRect(0, 100, 185, 150))
        font = QtGui.QFont()
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("")
        self.button_1.setText("")
        self.button_1.setCheckable(False)
        self.button_1.setChecked(False)
        self.button_1.setAutoDefault(False)
        self.button_1.setDefault(False)
        self.button_1.setFlat(True)
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(Form)
        self.button_2.setGeometry(QtCore.QRect(186, 100, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_2.setFont(font)
        self.button_2.setText("")
        self.button_2.setFlat(True)
        self.button_2.setObjectName("button_2")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(356, 100, 31, 451))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.button_3 = QtWidgets.QPushButton(Form)
        self.button_3.setGeometry(QtCore.QRect(372, 100, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_3.setFont(font)
        self.button_3.setText("")
        self.button_3.setFlat(True)
        self.button_3.setObjectName("button_3")
        self.button_4 = QtWidgets.QPushButton(Form)
        self.button_4.setGeometry(QtCore.QRect(0, 250, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_4.setFont(font)
        self.button_4.setText("")
        self.button_4.setFlat(True)
        self.button_4.setObjectName("button_4")
        self.button_6 = QtWidgets.QPushButton(Form)
        self.button_6.setGeometry(QtCore.QRect(372, 250, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_6.setFont(font)
        self.button_6.setText("")
        self.button_6.setFlat(True)
        self.button_6.setObjectName("button_6")
        self.button_5 = QtWidgets.QPushButton(Form)
        self.button_5.setGeometry(QtCore.QRect(186, 250, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_5.setFont(font)
        self.button_5.setText("")
        self.button_5.setFlat(True)
        self.button_5.setObjectName("button_5")
        self.button_7 = QtWidgets.QPushButton(Form)
        self.button_7.setGeometry(QtCore.QRect(0, 400, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_7.setFont(font)
        self.button_7.setText("")
        self.button_7.setFlat(True)
        self.button_7.setObjectName("button_7")
        self.button_9 = QtWidgets.QPushButton(Form)
        self.button_9.setGeometry(QtCore.QRect(372, 400, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_9.setFont(font)
        self.button_9.setText("")
        self.button_9.setFlat(True)
        self.button_9.setObjectName("button_9")
        self.button_8 = QtWidgets.QPushButton(Form)
        self.button_8.setGeometry(QtCore.QRect(186, 400, 185, 150))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.button_8.setFont(font)
        self.button_8.setText("")
        self.button_8.setFlat(True)
        self.button_8.setObjectName("button_8")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(0, 89, 551, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(0, 240, 554, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(0, 390, 554, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(0, 540, 554, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

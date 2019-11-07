import re #Regular Expression
import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi

path = f"{os.getcwd()}\\ui\\"

def stringRegEx(string):
    exp = re.search(r'^[a-zA-Z]+$',string)
    return exp

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        loadUi(f"{path}main.ui",self)
        self.second.clicked.connect(self.openSecondExercise)

    def openSecondExercise(self):
        self.hide()
        newWidget = secondExercise(self)
        newWidget.show()

class secondExercise(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(secondExercise, self).__init__(parent)
        loadUi(f"{path}second.ui",self)
        self.string.textChanged.connect(self.checkString)

    def checkString(self):
        if(self.string.isModified()):
            if(stringRegEx(self.string.text())):
                self.validation.setText(self.getFrecuency(self.string.text()))

    def getFrecuency(self, string):
        frecuency = {}
        for i in string:
            if i in frecuency:
                frecuency[i] += 1
            else:
                frecuency[i] = 1
        for i in frecuency:
            if(self.validFrecuency(frecuency, frecuency[i])):
                return "Yes"
            else:
                continue
        return "No"
    
    def validFrecuency(self, vector, value):
        count = 0
        for i in vector:
            if(value != vector[i]):
                count += abs(value - vector[i])
                if(count > 1):
                    return False
        return True

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
#coding: utf-8

import sys,io
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.mainUI()
    
    def mainUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('文字区切り君')

        self.lineEdit = QLineEdit(self)
        self.button = QPushButton('区切る！',self)
        self.button.clicked.connect(self.buttonClicked)

        #layout
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lineEdit)
        self.vbox.addWidget(self.button)
        

        self.setLayout(self.vbox)
        self.show()
    
    def buttonClicked(self):
        if(self.lineEdit.text() is None):
            pass
        contents = str(self.lineEdit.text())
        chars = list(contents)
        strings = '/'.join(chars)

        f = open('textfile.txt', 'w')
        f.write(strings)
        f.close()

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Main()
    sys.exit(app.exec_())
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


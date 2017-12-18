#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QVBoxLayout, QGroupBox)
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QScrollArea
from PyQt5.QtGui import QFont

class SemGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.vint = 0
        self.initUI()

    def initUI(self):
        grid = QVBoxLayout()
        grid.addWidget(self.itemToGrid())
        grid.addWidget(self.itemToGrid())
        grid.addWidget(self.itemToGrid())
        grid.addWidget(self.itemToGrid())
       # scroll = QScrollArea()
        #scroll.addWidget()
        self.setLayout(grid)
        self.setAutoFillBackground(True)
        self.setGeometry(300, 300, 500, 300)
        self.show()
    def itemToGrid(self):
        groupBox = QGroupBox()
        label1 = QLabel("one")
        label2 = QLabel("two")
        #label1.mouseReleaseEvent = self.showText1
        btn1 = QPushButton("open")
        btn2 = QPushButton("update")
        btn3 = QPushButton("preview")

        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        #hbox.addStretch(1)
        groupBox.mouseReleaseEvent = self.showText1
        groupBox.setLayout(hbox)
        return groupBox
    def showText1(self, event):
        print(event)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = SemGUI()
    sys.exit(app.exec_())
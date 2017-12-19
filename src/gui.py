#!/usr/bin/python3
import sys, sem, os
import subprocess 
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QVBoxLayout, QGroupBox)
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QScrollArea, QComboBox,  QLineEdit
from PyQt5.QtGui import QFont

class SemGUI(QWidget):
    def __init__(self,hashgraph):
        super().__init__()
        self.hashgraph = hashgraph
        self.initUI()
        

    def initUI(self):

        grid = QVBoxLayout()
        tgrid = QVBoxLayout()
        
        groupBox = QGroupBox()
        
        for key, value in self.hashgraph.items():
            tgrid.addWidget(self.itemToGrid(key, value))
        groupBox.setLayout(tgrid)
        
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        #scroll.setWidgetResizable(True)
        #scroll.setFixedWidth(1400)
        #to add above (like toolbar)
        #grid.addWidget(QPushButton("one"))
        
        #toolbar
        tbgrpbx = QGroupBox()
        tbhbox = QHBoxLayout()
        
        tbhbox.addWidget(QLineEdit())
        tbhbox.addWidget(QPushButton("search"))
        tbhbox.addWidget(QPushButton("reset"))
        tbhbox.addWidget(QPushButton("update DB"))
        tbgrpbx.setLayout(tbhbox)

        grid.addWidget(tbgrpbx)
        grid.addWidget(scroll)

        self.setLayout(grid)
        self.setAutoFillBackground(True)
        self.setGeometry(300, 300, 500, 300)
        self.show()
    def itemToGrid(self, key, value):
        name = value['info']['name']
        groupBox = QGroupBox()
        label1 = QLabel("Key: ")
        label2 = QLabel(key)
        #label1 = QLabel("Name:✔️")
        label1 = QLabel("Name:❤️")
        n = name.strip(' ')
        if(len(name) > 40):
            n = n[0:40]
        label2 = QLabel(n)
        #qbox = QComboBox()

        #qbox.addItems(value['dirs'])
        #label1.mouseReleaseEvent = self.showText1
        btn1 = QPushButton("open")
        btn1.clicked.connect(lambda event: self.openpdf(event,value['dirs'][0]))
        
        btn3 = QPushButton("preview")

        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        #hbox.addWidget(qbox)
        hbox.addWidget(btn1)
        hbox.addWidget(btn3)
        #hbox.addStretch(1)
        #groupBox.mouseReleaseEvent = self.showText1
        groupBox.mouseReleaseEvent = lambda event: self.showText1(event, value)
        groupBox.setLayout(hbox)
        return groupBox
    def showText1(self, event, value):
        print(value)
    def openpdf(self,event, value):
        subprocess.call(["xdg-open", value])
        print(value)
        
if __name__ == '__main__':
    s = sem.Sem()
    s.update_database()
    app = QApplication(sys.argv)
    
    #s.read_from_disk('../myhashmap.json')
    #s.print_hashmap()
    myapp = SemGUI(s.get_hashgraph())
    sys.exit(app.exec_())
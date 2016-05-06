#!/usr/bin/python
# -*- coding: utf-8 -*-
# quitbutton.py

import sys
from PyQt4 import QtGui, QtCore




class ColorDialog(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        color = QtGui.QColor(400, 100, 650)
        self.setGeometry(400, 100, 650, 600)
        self.setWindowTitle('ColorDialog')
        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.setFocus()
        self.widget = QtGui.QWidget(self)
        self.widget.setStyleSheet("QWidget { background-color: %s }" % color.name())
        self.widget.setGeometry(130, 22, 100, 100)

    def showDialog(self):
        color = QtGui.QColorDialog.getColor()
        self.widget.setStyleSheet("Qwidget { backround-color: %s } )" % color.name())

app = QtGui.QApplication(sys.argv)
qb = ColorDialog()
qb.show()
sys.exit(app.exec_())
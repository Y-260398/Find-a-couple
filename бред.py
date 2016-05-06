#!/usr/bin/python
# -*- coding: utf-8 -*-
# quitbutton.py

import sys
import pygame
from PyQt4 import QtGui, QtCore\

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red = ( 255,   0,   0)
green = (0,255,150)

pygame.init()

size=[650,600]
screen=pygame.display.set_mode(size)

pygame.display.set_caption('S.C.A.W')

done=False
clock=pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True


class MainWindow(QtGui.QMainWindow):
     def __init__(self):


      QtGui.QWidget.__init__(self, parent=None)

      self.setGeometry(400,100, 650, 600)
      self.setWindowTitle('32KGame')

      quit = QtGui.QPushButton(u'Close', self)
      quit.setGeometry(260, 400, 150, 100)           #1.X 2.Y 3.Len 4.size
      self.connect(quit, QtCore.SIGNAL('clicked()'),
          QtGui.qApp, QtCore.SLOT('quit()'))

      start = QtGui.QPushButton(u"Start",self)
      start.setGeometry(260, 10, 150, 100)
      self.connect(start, QtCore.SIGNAL('clicked()'),
         QtGui.qApp, QtCore.SLOT('start()'))


      options = QtGui.QPushButton(u"Options",self)
      options.setGeometry(260, 140, 150, 100)
      self.connect(options, QtCore.SIGNAL('clicked()'),
         QtGui.qApp, QtCore.SLOT('Options()'))

      faq = QtGui.QPushButton(u"Options",self)
      faq.setGeometry(260, 270, 150, 100)
      self.connect(faq, QtCore.SIGNAL('clicked()'),
         QtGui.qApp, QtCore.SLOT('FAQ()'))




app = QtGui.QApplication(sys.argv)
qb = MainWindow()
qb.show()


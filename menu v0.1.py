import sys
import pygame
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtGui




class Form(QDialog,QMainWindow):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)

      super(Form, self)
      self.setGeometry(50, 50, 750, 500)

      layout = QVBoxLayout()
      self.b1 = QPushButton("Button1")
      self.b1.setCheckable(True)
      self.b1.toggle()
      self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
      self.b1.clicked.connect(self.btnstate)
      self.b1.resize(50,500)
      layout.addWidget(self.b1)

      self.b2 = QPushButton()
      self.b2.setIcon(QIcon(QPixmap("t.jpg")))
      self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.b3 = QPushButton("Disabled")
      self.b3.setEnabled(False)
      layout.addWidget(self.b3)

      self.b4 = QPushButton("&Default")
      self.b4.setDefault(True)
      self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
      layout.addWidget(self.b4)

      self.setWindowTitle("Button demo")

   def btnstate(self):
      if self.b1.isChecked():
         print "button pressed"
      else:
         print "button released"

   def whichbtn(self,b):
      print "clicked button is "+b.text()

def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
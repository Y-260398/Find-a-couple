      start = QtGui.QPushButton(u"Start",self)
        start.setGeometry(5, 5, 100, 20)
        start.setGeometry(260, 10, 150, 100)
        self.connect(start, QtCore.SIGNAL('clicked()'),
             QtGui.qApp, QtCore.SLOT('start()'))
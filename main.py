import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class mainpage(QDialog):
    def __init__(self):
        super(mainpage,self).__init__()
        loadUi("idfk.ui",self)
        self.visabutton.clicked.connect(self.gotovisa)
        self.mastercardbutton.clicked.connect(self.gotomastercard)



    def gotovisa(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomastercard(self):
        widget.setCurrentIndex(widget.currentIndex()+2)



class Visa(QDialog):
    def __init__(self):
        super(Visa,self).__init__()
        loadUi("visa.ui",self)





class Mastercard(QDialog):
    def __init__(self):
        super(Mastercard,self).__init__()
        loadUi("mastercard.ui",self)


app = QApplication(sys.argv)
mainwin = mainpage()
widget = QtWidgets.QStackedWidget()
secondwidget = Visa()
thirdwidget = Mastercard()
widget.addWidget(mainwin)
widget.addWidget(secondwidget)
widget.addWidget(thirdwidget)
widget.setFixedWidth(521)
widget.setFixedHeight(351)
widget.show()
app.exec_()
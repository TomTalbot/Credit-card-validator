import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont




class mainpage(QDialog):
    def __init__(self):
        super(mainpage,self).__init__()
        loadUi("idfk.ui",self)

        #once specific button pressed, run the stack incrementaion counter
        self.visabutton.clicked.connect(self.gotovisa)
        self.mastercardbutton.clicked.connect(self.gotomastercard)

    # increments the stack counter by 1 to flip page
    def gotovisa(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomastercard(self):
        widget.setCurrentIndex(widget.currentIndex()+2)



class Visa(QDialog):
    def __init__(self):
        super(Visa,self).__init__()
        loadUi("visa.ui",self)
        self.verifybutton1.clicked.connect(self.validate)


    def validate(self):
        cardlist = []

        #takes input from the line edit box
        userinput = self.visatextbox.text()
        carduserinput = self.visatextbox.text()
        cardlist.append(carduserinput)
        print(cardlist)

        if len(userinput) != 16:
            message = QMessageBox()
            message.setWindowTitle("ERROR")
            message.setText("Visa cards contain 16 digits, try again.")

            x = message.exec_()


        if userinput.isalpha()== True:
            message = QMessageBox()
            message.setWindowTitle("ERROR")
            message.setText("This input contains letters")

            x = message.exec_()

        if cardlist[0] != 4:
            message = QMessageBox()
            message.setWindowTitle("ERROR")
            message.setText("Visa cards start with the digit 4")

            x = message.exec_()

        else:
            message = QMessageBox()
            message.setWindowTitle("SUCCESS")
            message.setText("Card Validated!.")







class Mastercard(QDialog):
    def __init__(self):
        super(Mastercard,self).__init__()
        loadUi("mastercard.ui",self)






app = QApplication(sys.argv)

#declaring stack and its widgets
mainwin = mainpage()
widget = QtWidgets.QStackedWidget()
secondwidget = Visa()
thirdwidget = Mastercard()

#adds widgets to the stacked widget
widget.addWidget(mainwin)
widget.addWidget(secondwidget)
widget.addWidget(thirdwidget)

#misc declarations
validator = QIntValidator()
widget.setFixedWidth(521)
widget.setFixedHeight(351)
widget.show()
app.exec_()
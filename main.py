import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
import pyluhn
from pyluhn import verify

#LOLOLOL couldve just used the FL package and had this whole project done in like 5 lines of code


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
        userinput = self.visatextbox.text() #takes user input
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


        else:
            verification = verify(userinput) #utilises Pyluhn library
            print(verification)
            if verification == True:
                message = QMessageBox() #creates message box instance
                message.setWindowTitle("Success")
                message.setText("This card is valid!")

                x = message.exec_() #displays message box

            else:
                message = QMessageBox()
                message.setWindowTitle("ERROR")
                message.setText("This card is invalid!")

                x = message.exec_()



class Mastercard(QDialog):
    def __init__(self):
        super(Mastercard,self).__init__()
        loadUi("mastercard.ui",self)
        self.verifybutton2.clicked.connect(self.validate) #links button to validate function


    def validate(self):
        cardlist= []

        #takes input from the line edit box
        userinput = self.mastercardtextbox.text()
        carduserinput = self.mastercardtextbox.text()
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


        else:
            verification = verify(userinput)
            print(verification)
            if verification == True:
                message = QMessageBox()
                message.setWindowTitle("Success")
                message.setText("This card is valid!")

                x = message.exec_()
            else:
                message = QMessageBox()
                message.setWindowTitle("ERROR")
                message.setText("This card is invalid!")

                x = message.exec_()



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
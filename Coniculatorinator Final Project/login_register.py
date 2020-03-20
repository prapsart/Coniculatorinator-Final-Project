from sqlitedict import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from main_menu import *

userrecorddb = SqliteDict("user_register.db", autocommit = True)    # Opening/Accessing a .db file
record = userrecorddb.get("record",[])   # Creates a list to contain dictionaries of user info


class LoginWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "User Login"
        self.__x = 750
        self.__y = 450
        self.__width = 300
        self.__height = 100
        self.userinterface()
                    
        self.setLayout(self.layout)
        self.show()
    
    def setXPosition(self, xposition): # set and get methods for Encapsulation
        self.__x = xposition
    def getXPosition(self):
        return self.__x
    def setYPosition(self, yposition):
        self.__y = yposition
    def getYPosition(self):
        return self.__y
    def setWidth(self, width):
        self.__width = width
    def getWidth(self):
        return self.__width
    def setHeight(self, height):
        self.__height = height
    def getHeight(self):
        return self.__height
    
    def userinterface(self):
        self.setWindowIcon(QIcon('sage'))
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: rgb(166, 191, 200);")
        self.setGeometry(self.getXPosition(), self.getYPosition(), self.getWidth(), self.getHeight())       
        self.layout = QGridLayout()
        
        self.layout.setColumnStretch(1,2)
        
        self.usernamelbl = QLabel ("Username ", self)
        self.usernamelbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.username = QLineEdit(self)
        self.username.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.layout.addWidget(self.usernamelbl, 0, 1)
        self.layout.addWidget(self.username, 0, 2)
        
        self.passwordlbl = QLabel("Password ", self)
        self.passwordlbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.password = QLineEdit(self)
        self.password.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.password.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.passwordlbl, 1, 1)
        self.layout.addWidget(self.password, 1, 2)
        
        self.regbttn = QPushButton('Register', self)
        self.regbttn.setShortcut('ctrl+O')
        self.regbttn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        self.regbttn.setToolTip("Don't have an account yet?")
        self.regbttn.clicked.connect(self.register)
        self.layout.addWidget(self.regbttn, 3, 1)
        
        self.logbttn = QPushButton('Log in', self)
        self.logbttn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        self.logbttn.setToolTip("Press login button to proceed")
        self.logbttn.clicked.connect(self.login)
        self.layout.addWidget(self.logbttn, 3, 2)
        
        self.exitbttn = QPushButton('Exit', self)
        self.exitbttn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        self.exitbttn.setToolTip("Click if you want to Exit.")
        self.exitbttn.clicked.connect(self.exitUser)
        self.layout.addWidget(self.exitbttn, 3, 3)
    
    # SLOTS/METHODS
    @pyqtSlot()
    def login(self): # Authenticates the user inputs
        login_list = [{'Username': self.username.text()},
                       {'Password': self.password.text()}]

        if (self.username.text() == '') and (self.password.text() == ''):
            QMessageBox.information(self, "Error!", "Please fill in all the fields!", QMessageBox.Ok, QMessageBox.Ok)
        
        elif (self.username.text() == '') or (self.password.text() == ''):
            for login in login_list:
                for key, value in login.items():
                    if value == '':
                        QMessageBox.warning(self, "Error!", f"Please fill in your {key}.", QMessageBox.Ok, QMessageBox.Ok)
        
        for records in record:
            if (self.username.text() == records['Username']) and (self.password.text() == records['Password']):
                QMessageBox.information(self, "Authentication","Login Successful!", QMessageBox.Ok, QMessageBox.Ok)
                self.mainMenu = MainWindow()
                self.close()
                self.mainMenu.show()
                break
            else:
                continue
                                
    def register(self): # Directs the user to the Register Window
        self.regbttn = RegisterWindow() 
        self.close()           
        self.regbttn.show() 
    
    def exitUser(self):    # Terminates the application
        QMessageBox.warning(self, "Exit", "Press 'OK to exit", QMessageBox.Ok, QMessageBox.Ok)
        self.close()    
    

class RegisterWindow(QWidget):   
     
    def __init__(self):
        super().__init__()
        self.__x = 750
        self.__y = 400
        self.__width = 400
        self.__height = 270
        self.title = "User Register"
        
        self.regiform()
        self.setLayout(self.layout)
        
        self.show()

    def setXPosition(self, xposition): # set and get methods for Encapsulation
        self.__x = xposition
    def getXPosition(self):
        return self.__x
    def setYPosition(self, yposition):
        self.__y = yposition
    def getYPosition(self):
        return self.__y
    def setWidth(self, width):
        self.__width = width
    def getWidth(self):
        return self.__width
    def setHeight(self, height):
        self.__height = height
    def getHeight(self):
        return self.__height
        
        
    def regiform(self):
        self.setWindowIcon(QIcon('sage'))
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color: rgb(166, 191, 200);")
        self.setGeometry(self.getXPosition(), self.getYPosition(), self.getWidth(), self.getHeight())
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1,2)

        self.fnamelbl = QLabel ("First Name", self)
        self.fnamelbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.fnametxt = QLineEdit(self)
        self.fnametxt.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.fnametxt.setPlaceholderText("Input your First Name")
        self.layout.addWidget(self.fnamelbl, 1.5, 1.5)
        self.layout.addWidget(self.fnametxt, 1.5, 2.5)

        self.lnamelbl = QLabel ("Last Name", self)
        self.lnamelbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.lnametxt = QLineEdit(self)
        self.lnametxt.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.lnametxt.setPlaceholderText("Input your Last Name")
        self.layout.addWidget(self.lnamelbl, 2, 1)
        self.layout.addWidget(self.lnametxt, 2, 2)

        self.usernamelbl = QLabel ("Username", self)
        self.usernamelbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.usernametxt = QLineEdit(self)
        self.usernametxt.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.usernametxt.setPlaceholderText("Input your Username")
        self.layout.addWidget(self.usernamelbl, 3, 1)
        self.layout.addWidget(self.usernametxt, 3, 2)

        self.passlbl = QLabel ("Password", self)
        self.passlbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.passtxt = QLineEdit(self)
        self.passtxt.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.passtxt.setEchoMode(QLineEdit.Password)
        self.passtxt.setPlaceholderText("Input your Password")
        self.layout.addWidget(self.passlbl, 4, 1)
        self.layout.addWidget(self.passtxt, 4, 2)

        self.emaillbl = QLabel ("Email", self)
        self.emaillbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.emailtxt = QLineEdit(self)
        self.emailtxt.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.emailtxt.setPlaceholderText("Input your Email")
        self.layout.addWidget(self.emaillbl, 5, 1)
        self.layout.addWidget(self.emailtxt, 5, 2)

        self.contactlbl = QLabel ("Contact Number", self)
        self.contactlbl.setStyleSheet("font: 12pt \"Bauhaus 93\";")
        self.contacttxt = QLineEdit(self)
        self.contacttxt.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.contacttxt.setPlaceholderText("Input your Contact No.")
        self.layout.addWidget(self.contactlbl, 6, 1)
        self.layout.addWidget(self.contacttxt, 6, 2)
        
        self.subbttn = QPushButton('Register', self)
        self.subbttn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        self.subbttn.setShortcut('ctrl+S')
        self.subbttn.setToolTip("Click to submit")
        self.subbttn.clicked.connect(self.submit)
        self.layout.addWidget(self.subbttn, 7, 2)
        
        self.clrbttn = QPushButton('Clear', self)
        self.clrbttn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        self.clrbttn.setToolTip("Clear all the fields")
        self.clrbttn.clicked.connect(self.clear)
        self.layout.addWidget(self.clrbttn, 7, 1)
        
        self.logbttn = QPushButton('Log in', self)
        self.logbttn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        self.logbttn.setToolTip("Already have an account?")
        self.logbttn.clicked.connect(self.login)
        self.layout.addWidget(self.logbttn, 7, 3)
        
    @pyqtSlot()
    def submit(self):   # Adds the user inputs to the database a dictionary with error handling     
        registration_list=[{'First Name': self.fnametxt.text()}, 
                            {'Last Name': self.lnametxt.text()}, 
                            {'Username': self.usernametxt.text()},
                            {'Password': self.passtxt.text()}, 
                            {'Email': self.emailtxt.text()}, 
                            {'Contact Number': self.contacttxt.text()}]
        
        buttonReply = QMessageBox.question(self, "Submit", "Are you sure you want to submit?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if (self.fnametxt.text() == '') and (self.lnametxt.text() == '') and (self.usernametxt.text() == '') and (self.passtxt.text() == '') and (self.emailtxt.text() == '') and (self.contacttxt.text() == ''):
            QMessageBox.warning(self, "Error!", "Please fill up all the boxes.", QMessageBox.Ok, QMessageBox.Ok)
        
        elif (self.fnametxt.text() == '') or (self.lnametxt.text() == '') or (self.usernametxt.text() == '') or (self.passtxt.text() == '') or (self.emailtxt.text() == '') or (self.contacttxt.text() == ''):
            for registration in registration_list:
                for key, value in registration.items():
                    if value == '':
                        QMessageBox.warning(self, "Error!", f"Please fill up {key}.", QMessageBox.Ok, QMessageBox.Ok)
                
        elif buttonReply == QMessageBox.Yes:
                record.append({'First Name': self.fnametxt.text().title(),  
                                    'Last Name': self.lnametxt.text().title(), 
                                    'Username': self.usernametxt.text(),
                                    'Password': self.passtxt.text(), 
                                    'Email': self.emailtxt.text(), 
                                    'Contact Number': self.contacttxt.text()
                                    })
                userrecorddb["record"] = record
                QMessageBox.information(self, "Register Successful", "The account has been successfully created.", QMessageBox.Ok, QMessageBox.Ok)
        

    def clear(self):    # Clears all user input inside the text fields
        self.fnametxt.clear()
        self.lnametxt.clear()
        self.usernametxt.clear()
        self.passtxt.clear()
        self.emailtxt.clear()
        self.contacttxt.clear()
        
    def login(self):    # Directs the user to the login window
        self.loginWindow = LoginWindow()
        self.close()
        self.loginWindow.show()


# This file is the one to be run. It serves as the launcher and shall not ran when imported.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow() 
    sys.exit(app.exec_())        
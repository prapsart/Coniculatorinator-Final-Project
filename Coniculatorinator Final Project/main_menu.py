import math             # Importation of math library
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *             # Importation of PyQt5
from PyQt5.QtCore import pyqtSlot
from oop_conic_sections import *    # Importation of the files with User-defined Classes

class MainWindow(QMainWindow): # Main Window - contains the menu bar and other windows

    def __init__(self):
        super().__init__()
        self.__x = 750
        self.__y = 450
        self.__width = 300
        self.__height = 100
        self.setGeometry(self.getXPosition(), self.getYPosition(), self.getWidth(), self.getHeight()) 
        self.setWindowTitle("ConiCulator-Inator")
        self.setWindowIcon(QIcon('sage'))
        self.setStyleSheet("background-color: rgb(166, 191, 200);")
        self.loadmenu()
        self.loadwidget()
        
        self.show()

    def setXPosition(self, xposition):
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
    

    def loadmenu(self): 
        mainMenu = self.menuBar()
        optionMenu = mainMenu.addMenu('Options')
        optionMenu.setStyleSheet("color: rgb(250,255, 255);")
        optionMenu.setStyleSheet("font: 10pt \"Tw Cen MT 93\";")

        exitButton = QAction('Exit',self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        optionMenu.addAction(exitButton)

    def loadwidget(self):
        self.MainMenu = MainMenu()
        self.setCentralWidget(self.MainMenu)
        

class MainMenu(QWidget): # Menu Bar 
    def __init__(self):
        super(MainMenu,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1,2)
        self.setStyleSheet("background-color: rgb(166, 191, 200);")
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        
        titlelbl = QLabel("       CONICULATORINATOR",self)
        titlelbl.move(50, 30)
        titlelbl.setStyleSheet("font: 15pt \"Bauhaus 93\";")

        identifier_btn = QPushButton("Conic type identifier",self)
        identifier_btn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        identifier_btn.clicked.connect(self.identifier)
        self.layout.addWidget(identifier_btn, 2, 1)
        
        circle_btn = QPushButton("Circle",self)
        circle_btn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        circle_btn.clicked.connect(self.circleWindow)
        self.layout.addWidget(identifier_btn, 3, 1)
        
        parabola_btn = QPushButton("Parabola",self)
        parabola_btn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        parabola_btn.clicked.connect(self.parabolaWindow)
        self.layout.addWidget(identifier_btn, 4, 1)
        
        ellipse_btn = QPushButton("Ellipse",self)
        ellipse_btn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        ellipse_btn.clicked.connect(self.ellipseWindow)
        self.layout.addWidget(identifier_btn, 5, 1)
        
        hyperbola_btn = QPushButton("Hyperbola",self)
        hyperbola_btn.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        hyperbola_btn.clicked.connect(self.hyperbolaWindow)
        self.layout.addWidget(identifier_btn, 6, 1)
        
        list_buttons = (identifier_btn,circle_btn,parabola_btn,ellipse_btn,hyperbola_btn)
        vbox.addWidget(titlelbl)

        vbox.addStretch()
        for button in list_buttons:
            vbox.addWidget(button)
        vbox.addStretch()

    # SLOTS/METHODS of each buttons in Main Window
    @pyqtSlot() 
    def circleWindow(self):
        self.circle_dialog = CircleWindow() # Creates an instance for the circle window
        self.circle_dialog.show()   # Opens the circle window

    def parabolaWindow(self):
        self.parabola_dialog = ParabolaWindow() # Creates an instance for the parabola window
        self.parabola_dialog.show() # Opens the parabola window

    def ellipseWindow(self):
        self.ellipse_dialog = EllipseWindow()   # Creates an instance for the ellipse window
        self.ellipse_dialog.show()  # Opens the ellipse window

    def hyperbolaWindow(self):
        self.hyperbola_dialog = HyperbolaWindow()   # Creates an instance for the hyperbola window
        self.hyperbola_dialog.show()    # Opens the hyperbola window

    def identifier(self):
        self.identifier_dialog = IdentifierWindow() # Creates an instance for the identifier window
        self.identifier_dialog.show()   # Opens the identifier window


class CircleWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle")
        self.setGeometry(780,400,260,300)
        self.setWindowIcon(QIcon('sage'))
        self.setStyleSheet("background-color: rgb(166, 191, 200);")
        self.initUI()
        self.setLayout(self.layout)
        
    
    def initUI(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1,3)
        
        xpluslabel = QLabel("( X +",self)
        xpluslabel.setStyleSheet("font: 11pt \"Arial\";")
        xpluslabel.move(20,30)
        
        self.htextbox = QLineEdit(self)
        self.htextbox.setPlaceholderText("H")
        self.htextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.htextbox.setGeometry(53,38,30,15)
        
        cplabel = QLabel(")² +",self)
        cplabel.setStyleSheet("font: 11pt \"Arial\";")
        cplabel.move(85,30)
        
        ypluslabel = QLabel("( Y +",self)
        ypluslabel.setStyleSheet("font: 11pt \"Arial\";")
        ypluslabel.move(110,30)
        
        self.ktextbox = QLineEdit(self)
        self.ktextbox.setPlaceholderText("K")
        self.ktextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.ktextbox.setGeometry(143,38,30,15)
        
        cp2label = QLabel(")²",self)
        cp2label.setStyleSheet("font: 11pt \"Arial\";")
        cp2label.move(175,30)
        
        equallbl = QLabel(" = ",self)
        equallbl.setStyleSheet("font: 11pt \"Arial\";")
        equallbl.move(185,30)
        
        self.equaltxtbox = QLineEdit(self)
        self.equaltxtbox.setPlaceholderText("R²")
        self.equaltxtbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.equaltxtbox.setGeometry(205,38,30,15)
        
        calculate_button = QPushButton("Calculate",self)
        calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        calculate_button.clicked.connect(self.calculateCircleParts)
        calculate_button.move(85,70)
        
        view_graph_button = QPushButton("View Graph",self)
        view_graph_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        view_graph_button.clicked.connect(self.graphCircle)
        view_graph_button.move(85,230)
        
        self.result = QTextEdit(self)
        self.result.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
        self.result.setGeometry(10,110,240,100)

    @pyqtSlot()
    def calculateCircleParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.r = (int(self.equaltxtbox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            radius = math.sqrt(self.r)
            diameter = 2*radius
            endpt1 = (self.h+radius,self.k)
            endpt2 = (self.h-radius,self.k)
            endpt3 = (self.h,self.k+radius)
            endpt4 = (self.h,self.k-radius)

            information = f"CENTER ({self.h},{self.k})\nRADIUS = {radius}\nDIAMETER = {diameter}\nEndpoints {endpt1},{endpt2},{endpt3},{endpt4}"
            self.result.setText(information)

    
    def graphCircle(self):
        try:
            circle_object = Circle(self.h,self.k,self.r)
            circle_object.graph_parts()
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
        

class ParabolaWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parabola")
        self.setWindowIcon(QIcon('sage'))
        self.setStyleSheet("background-color: rgb(166, 191, 200);")
        self.setGeometry(755,380,300,300)
        self.initUI()
    
    def initUI(self):
        upOrDownChoice = QMessageBox.question(self, "Question", "Does your major axis lie on Y-Axis?", QMessageBox.Yes, QMessageBox.No)
        if upOrDownChoice == QMessageBox.Yes:  # If the parabola is Upward/Downward (major axis on Y-Axis)
            xpluslabel = QLabel("( X +",self)
            xpluslabel.setStyleSheet("font: 11pt \"Arial\";")
            xpluslabel.move(45,30)
            
            self.htextbox = QLineEdit(self)
            self.htextbox.setPlaceholderText("H")
            self.htextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.htextbox.setGeometry(78,30,30,15)
            
            cplabel = QLabel(")²  =",self)
            cplabel.setStyleSheet("font: 11pt \"Arial\";")
            cplabel.move(110,30)
            
            self.fourP = QLineEdit(self)
            self.fourP.setPlaceholderText("4P")
            self.fourP.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.fourP.setGeometry(143,30,30,15)
            
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.setStyleSheet("font: 11pt \"Arial\";")
            ypluslabel.move(175,30)
            
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setPlaceholderText("K")
            self.ktextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.ktextbox.setGeometry(208,30,30,15)
            
            cp2label = QLabel(")",self)
            cp2label.setStyleSheet("font: 11pt \"Arial\";")
            cp2label.move(240,30)
            
            calculate_button = QPushButton("Calculate",self)
            calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            calculate_button.move(110,60)
            calculate_button.clicked.connect(self.calculateUpDownParabolaParts)
            
            view_graph_button = QPushButton("View Graph",self)
            view_graph_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            view_graph_button.move(110,240)
            view_graph_button.clicked.connect(self.graphUpDownParabola)
            
            self.result = QTextEdit(self)
            self.result.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.result.setGeometry(10,100,280,130)
            
        else:      # If the parabola opens Right/Left (major axis on X-Axis)
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.setStyleSheet("font: 11pt \"Arial\";")
            ypluslabel.move(45,30)
            
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setPlaceholderText("K")
            self.ktextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.ktextbox.setGeometry(78,30,30,15)
            
            cplabel = QLabel(")²  =",self)
            cplabel.setStyleSheet("font: 11pt \"Arial\";")
            cplabel.move(110,30)
            
            self.fourP = QLineEdit(self)
            self.fourP.setPlaceholderText("4P")
            self.fourP.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.fourP.setGeometry(143,30,30,15)
            
            xpluslabel = QLabel("( X +",self)
            xpluslabel.setStyleSheet("font: 11pt \"Arial\";")
            xpluslabel.move(175,30)
            
            self.htextbox = QLineEdit(self)
            self.htextbox.setPlaceholderText("H")
            self.htextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.htextbox.setGeometry(208,30,30,15)
            
            cp2label = QLabel(")",self)
            cp2label.setStyleSheet("font: 11pt \"Arial\";")
            cp2label.move(240,30)
            
            calculate_button = QPushButton("Calculate",self)
            calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            calculate_button.move(110,60)
            calculate_button.clicked.connect(self.calculateRightLeftParabolaParts)
            
            view_graph_button = QPushButton("View Graph",self)
            view_graph_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            view_graph_button.move(110,240)
            view_graph_button.clicked.connect(self.graphRightLeftParabola)
            
            self.result = QTextEdit(self)
            self.result.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.result.setGeometry(10,100,280,130)
    
    @pyqtSlot()
    def calculateUpDownParabolaParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.fourp = round((int(self.fourP.text()))/4,2)
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            vertex = (self.h,self.k)
            focus = (self.h, self.k+(self.fourp))
            directrix = -((self.fourp)+self.k)
            lengthLR = (self.fourp)*4
            endptLRA = (self.h+(2*(self.fourp)),self.k)
            endptLRB = (self.h-(2*(self.fourp)),self.k)
            information = f'VERTEX {vertex}\nFOCUS {focus}\nDIRECTRIX y = {directrix}x\nLENGTH OF LR={lengthLR}\nENDPOINT-A LR {endptLRA}\nENDPOINT-B LR {endptLRB}'
            self.result.setText(information)

    def calculateRightLeftParabolaParts(self):
        try:
            self.hPRL = -(int(self.htextbox.text()))
            self.kPRL = -(int(self.ktextbox.text()))
            self.fourpPRL = round((int(self.fourP.text()))/4,2)
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            vertex = (self.hPRL,self.kPRL)
            focus = (self.hPRL+(self.fourpPRL), self.kPRL)
            directrix = -((self.fourpPRL)+self.hPRL)
            lengthLR = (self.fourpPRL)*4
            endptLRA = (self.hPRL,self.kPRL+(2*(self.fourpPRL)))
            endptLRB = (self.hPRL,self.kPRL-(2*(self.fourpPRL)))
            information = f'VERTEX {vertex}\nFOCUS {focus}\nDIRECTRIX x = {directrix}y\nLENGTH OF LR {lengthLR}\nENDPOINT-A LR {endptLRA} ENDPOINT-B LR {endptLRB}'
            self.result.setText(information)

    def graphUpDownParabola(self):
        try:
            updownParabola_object = UpDownParabola(self.h,self.k,self.fourp)
            updownParabola_object.graph_parts()
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
    
    def graphRightLeftParabola(self):
        try:
            rightLeftParabola_object = RightLeftParabola(self.hPRL,self.kPRL,self.fourpPRL)
            rightLeftParabola_object.graph_parts()
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
        

class EllipseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ellipse")
        self.setWindowIcon(QIcon('sage'))
        self.setGeometry(750,380,300,300)
        self.initUI()
    
    def initUI(self):
        XOrYChoice = QMessageBox.question(self, "Question", "Is the major axis of your ellipse lies on X axis?", QMessageBox.Yes, QMessageBox.No)
        if XOrYChoice == QMessageBox.Yes: # If the major axis lies on X-Axis
            xpluslabel = QLabel("( X +",self)
            xpluslabel.setStyleSheet("font: 11pt \"Arial\";")
            xpluslabel.move(40,30)
            
            self.htextbox = QLineEdit(self)
            self.htextbox.setPlaceholderText("H")
            self.htextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.htextbox.setGeometry(73,30,30,15)
            
            cplabel = QLabel(")² +",self)
            cplabel.setStyleSheet("font: 11pt \"Arial\";")
            cplabel.move(105,30)
            
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.setStyleSheet("font: 11pt \"Arial\";")
            ypluslabel.move(137,30)
            
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setPlaceholderText("K")
            self.ktextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.ktextbox.setGeometry(170,30,30,15)
            
            cp2label = QLabel(")²",self)
            cp2label.setStyleSheet("font: 11pt \"Arial\";")
            cp2label.move(202,30)
            
            equallbl = QLabel(" = ",self)
            equallbl.setStyleSheet("font: 11pt \"Arial\";")
            equallbl.move(220,30)
            
            equal1 = QLabel('1',self)
            equal1.setStyleSheet("font: 11pt \"Arial\";")
            equal1.setGeometry(250,30,20,15)
            
            _x  = QLabel("___________",self)
            _x.move(40,38)
            
            _y  = QLabel("___________",self)
            _y.move(137,38)
            
            self.aBox = QLineEdit(self)
            self.aBox.setPlaceholderText("A")
            self.aBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.aBox.setGeometry(58,60,30,15)
            
            self.bBox = QLineEdit(self)
            self.bBox.setPlaceholderText("B")
            self.bBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.bBox.setGeometry(158,60,30,15)
            
            calculate_button = QPushButton("Calculate",self)
            calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            calculate_button.move(110,80)
            calculate_button.clicked.connect(self.calculateEllipseXmajParts)
            
            view_graph_button = QPushButton('View Graph',self)
            view_graph_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            view_graph_button.move(110,240)
            view_graph_button.clicked.connect(self.graphEllipseXMaj)
            
            self.result = QTextEdit(self)
            self.result.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.result.setGeometry(10,110,280,120)

        else:   # If the major axis lies on Y-Axis
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.setStyleSheet("font: 11pt \"Arial\";")
            ypluslabel.move(30,30)
            
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setPlaceholderText("K")
            self.ktextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.ktextbox.setGeometry(73,30,30,15)
            
            cplabel = QLabel(")² +",self)
            cplabel.setStyleSheet("font: 11pt \"Arial\";")
            cplabel.move(105,30)
            
            xpluslabel = QLabel("( X +",self)
            xpluslabel.setStyleSheet("font: 11pt \"Arial\";")
            xpluslabel.move(137,30)
            
            self.htextbox = QLineEdit(self)
            self.htextbox.setPlaceholderText("H")
            self.htextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.htextbox.setGeometry(170,30,30,15)
            
            cp2label = QLabel(")²",self)
            cp2label.setStyleSheet("font: 11pt \"Arial\";")
            cp2label.move(202,30)
            
            equallbl = QLabel(" = ",self)
            equallbl.setStyleSheet("font: 11pt \"Arial\";")
            equallbl.move(220,30)
            
            equal1 = QLabel('1',self)
            equal1.setStyleSheet("font: 11pt \"Arial\";")
            equal1.setGeometry(250,30,20,15)
            
            _x  = QLabel("___________",self)
            _x.move(40,38)
            
            _y  = QLabel("___________",self)
            _y.move(137,38)
            
            self.aBox = QLineEdit(self)
            self.aBox.setPlaceholderText("A")
            self.aBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.aBox.setGeometry(58,60,30,15)
            
            self.bBox = QLineEdit(self)
            self.bBox.setPlaceholderText("B")
            self.bBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.bBox.setGeometry(158,60,30,15)
            
            calculate_button = QPushButton("Calculate",self)
            calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            calculate_button.move(110,80)
            calculate_button.clicked.connect(self.calculateEllipseYmajParts)
            
            view_graph_button = QPushButton('View Graph',self)
            view_graph_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            view_graph_button.move(110,240)
            view_graph_button.clicked.connect(self.graphEllipseYMaj)
            
            self.result = QTextEdit(self)
            self.result.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.result.setGeometry(10,110,280,120)
        
    @pyqtSlot()
    def calculateEllipseXmajParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.a > self.b:
                c = round(((self.a)**2 - (self.b)**2)**(1/2),2)
                center = (self.h,self.k)
                focus1 = (self.h+c,self.k)
                focus2 = (self.h-c,self.k)
                vertex1 = (self.h+self.a,self.k)
                vertex2 = (self.h-self.a,self.k)
                lengthLR = round(((2*(self.b**2))/self.a),2)
                lr1 = round(((self.b**2)/self.a),2)
                lr2 = round((-(self.b**2)/self.a),2) 
                endpt1LRA = (self.h+c,self.k+lr1)
                endpt2LRA = (self.h+c,self.k+lr2)
                endpt1LRB = (self.h-c,self.k+lr1)
                endpt2LRB = (self.h-c,self.k+lr2)
                eccentricity = round((c/self.a),2)

                information = f"CENTER{center}\nFOCUS1 {focus1}\nFOCUS2 {focus2}\nVERTEX1 {vertex1}\nVERTEX2 {vertex2}\nLENGTH OF LATERA RECTI={lengthLR}\nENDPOINT1A LR {endpt1LRA}\nENDPOINT1B LR{endpt1LRB}\nENDPOINT2A LR{endpt2LRA}\nENDPOINT2B LR{endpt2LRB}\nECCENTRICITY = {eccentricity} " 
                self.result.setText(information)
            else:
                QMessageBox.warning(self, "Error", "Value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)

    def calculateEllipseYmajParts(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.a > self.b:
                c = round(((self.a)**2 - (self.b)**2)**(1/2),2)
                center = (self.h,self.k)
                focus1 = (self.h,self.k+c)
                focus2 = (self.h,self.k-c)
                vertex1 = (self.h,self.k+self.b)
                vertex2 = (self.h,self.k-self.b)
                lengthLR = (2*(self.a**2))/self.b
                lr1 = (self.a**2)/self.b
                lr2 = -(self.a**2)/self.b 
                endpt1LRA = (self.h+lr1,self.k+c)
                endpt2LRA = (self.h+lr2,self.k+c)
                endpt1LRB = (self.h+lr1,self.k-c)
                endpt2LRB = (self.h+lr2,self.k-c)
                eccentricity = c/self.a

                information = f"CENTER{center}\nFOCUS1 {focus1} FOCUS2{focus2}\nVERTEX1 {vertex1}\nVERTEX2 {vertex2}\nLENGTH OF LATERA RECTI={lengthLR}\nENDPOINT1A LR{endpt1LRA}\nENDPOINT1B LR{endpt2LRA}\nENDPOINT2A LR{endpt1LRA}\nENDPOINT2B LR{endpt2LRB}\nECCENTRICITY = {eccentricity}" 
                self.result.setText(information)
            else:
                QMessageBox.warning(self, "Error", "Value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)

    def graphEllipseXMaj(self):
        try:
            if self.a > self.b:
                ellipseXmaj_object = EllipseXmaj(self.a,self.b,self.h,self.k)
                ellipseXmaj_object.graph_parts()
            else:
                QMessageBox.warning(self, "Error", "Value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)

    def graphEllipseYMaj(self):
        try:
            if self.a > self.b:
                ellipseYmaj_object = EllipseYmaj(self.b,self.a,self.h,self.k)
                ellipseYmaj_object.graph_parts()
            else:
                QMessageBox.warning(self, "Error", "Value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
    

class HyperbolaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hyperbola")
        self.setWindowIcon(QIcon('sage'))
        self.setGeometry(750,380,300,330)
        self.initUI()
    
    def initUI(self):
        XOrYChoice = QMessageBox.question(self, "Question", "Is your major axis on X-Axis?", QMessageBox.Yes, QMessageBox.No)
        if XOrYChoice == QMessageBox.Yes:   # If the major axis lies on X-Axis
            xpluslabel = QLabel("( X +",self)
            xpluslabel.setStyleSheet("font: 11pt \"Arial\";")
            xpluslabel.move(30,30)
            
            self.htextbox = QLineEdit(self)
            self.htextbox.setPlaceholderText("H")
            self.htextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.htextbox.setGeometry(73,30,30,15)
            
            cplabel = QLabel(")² -",self)
            cplabel.setStyleSheet("font: 11pt \"Arial\";")
            cplabel.move(105,30)
            
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.setStyleSheet("font: 11pt \"Arial\";")
            ypluslabel.move(137,30)
            
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setPlaceholderText("K")
            self.ktextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.ktextbox.setGeometry(170,30,30,15)
            
            cp2label = QLabel(")²",self)
            cp2label.setStyleSheet("font: 11pt \"Arial\";")
            cp2label.move(202,30)
            
            equallbl = QLabel(" = ",self)
            equallbl.setStyleSheet("font: 11pt \"Arial\";")
            equallbl.move(220,30)
            
            equal1 = QLabel('1',self)
            equal1.setStyleSheet("font: 11pt \"Arial\";")
            equal1.setGeometry(250,30,20,15)
            
            _x  = QLabel("___________",self)
            _x.move(40,38)
            
            _y  = QLabel("___________",self)
            _y.move(137,38)
            
            self.aBox = QLineEdit(self)
            self.aBox.setPlaceholderText("A")
            self.aBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.aBox.setGeometry(58,60,30,15)
            
            self.bBox = QLineEdit(self)
            self.bBox.setPlaceholderText("B")
            self.bBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.bBox.setGeometry(158,60,30,15)
            
            calculate_button = QPushButton("Calculate",self)
            calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            calculate_button.move(110,85)
            calculate_button.clicked.connect(self.calculateHyperbolaXmaj)
            
            view_graph_button = QPushButton("View",self)
            view_graph_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            view_graph_button.move(140,260)
            view_graph_button.clicked.connect(self.graphHyperbolaXmaj)
            
            self.result = QTextEdit(self)
            self.result.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.result.setGeometry(10,130,280,120)

        elif XOrYChoice == QMessageBox.No:  # If the major axis lies on Y-Axis
            ypluslabel = QLabel("( Y +",self)
            ypluslabel.setStyleSheet("font: 11pt \"Arial\";")
            ypluslabel.move(30,30)
            
            self.ktextbox = QLineEdit(self)
            self.ktextbox.setPlaceholderText("K")
            self.ktextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.ktextbox.setGeometry(73,30,30,15)
            
            cplabel = QLabel(")² -",self)
            cplabel.setStyleSheet("font: 11pt \"Arial\";")
            cplabel.move(105,30)
            
            xpluslabel = QLabel("( X +",self)
            xpluslabel.setStyleSheet("font: 11pt \"Arial\";")
            xpluslabel.move(137,30)
            
            self.htextbox = QLineEdit(self)
            self.htextbox.setPlaceholderText("H")
            self.htextbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.htextbox.setGeometry(170,30,30,15)
            
            cp2label = QLabel(")²",self)
            cp2label.setStyleSheet("font: 11pt \"Arial\";")
            cp2label.move(202,30)
            
            equallbl = QLabel(" = ",self)
            equallbl.setStyleSheet("font: 11pt \"Arial\";")
            equallbl.move(220,30)
            
            equal1 = QLabel('1',self)
            equal1.setStyleSheet("font: 11pt \"Arial\";")
            equal1.setGeometry(250,30,20,15)
            
            _x  = QLabel("___________",self)
            _x.move(40,38)
            
            _y  = QLabel("___________",self)
            _y.move(137,38)
            
            self.aBox = QLineEdit(self)
            self.aBox.setPlaceholderText("A")
            self.aBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.aBox.setGeometry(58,60,30,15)
            
            self.bBox = QLineEdit(self)
            self.bBox.setPlaceholderText("B")
            self.bBox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.bBox.setGeometry(158,60,30,15)
            
            calculate_button = QPushButton("Calculate",self)
            calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            calculate_button.move(110,85)
            calculate_button.clicked.connect(self.calculateHyperbolaYmaj)
            
            view_graph_button = QPushButton("View",self)
            view_graph_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
            view_graph_button.move(140,260)
            view_graph_button.clicked.connect(self.graphHyperbolaYmaj)
            
            self.result = QTextEdit(self)
            self.result.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
            self.result.setGeometry(10,130,280,120)

    @pyqtSlot()
    def calculateHyperbolaXmaj(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.a > self.b:
                c = round((((self.b**2)+(self.a**2))**(1/2)),2)
                center = (self.h,self.k)
                focus1 = (self.h,self.k+c)
                focus2 = (self.h,self.k-c)
                vertex1 = (self.h,self.k+self.a)
                vertex2 = (self.h,self.k-self.a)

                b_over_a = round((self.b/self.a),2)
                if (center[0]<0) and (center[0]<0):
                    asymp_eq = f'(x+{center[0]})=±{b_over_a}(y+{center[1]})'
                elif (center[0]>0) and (center[1]<0):
                    asymp_eq = f'(x+{center[0]})=±{b_over_a}(y-{center[1]})'
                elif (center[0]<0) and (center[1]>0):
                    asymp_eq = f'(x-{center[0]})=±{b_over_a}(y+{center[1]})'
                else:
                    asymp_eq = f'(x-{center[0]})=±{b_over_a}(y-{center[1]})'

                information = f"CENTER{center}\nFOCUS1{focus1}\nFOCUS2{focus2}\nVERTEX1{vertex1}\nVERTEX2{vertex2}\nASYMPTOTE EQUATION:{asymp_eq}"
                self.result.setText(information)

            else:
                QMessageBox.warning(self, "Error", "The value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)

    def graphHyperbolaXmaj(self):
        try:
            if self.a > self.b:
                hyperbolaXmaj_object = HyperbolaXmaj(self.a,self.b,self.h,self.k)
                hyperbolaXmaj_object.graph_parts()
            else:
                QMessageBox.warning(self, "Error", "The value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)
    
    def calculateHyperbolaYmaj(self):
        try:
            self.h = -(int(self.htextbox.text()))
            self.k = -(int(self.ktextbox.text()))
            self.a = (int(self.aBox.text()))
            self.b = (int(self.bBox.text()))
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.a >= self.b:
                c = round((((self.b**2)+(self.a**2))**(1/2)),2)
                center = (self.h,self.k)
                focus1 = (self.h+c,self.k)
                focus2 = (self.h-c,self.k)
                vertex1 = (self.h+self.a,self.k)
                vertex2 = (self.h-self.a,self.k)
                b_over_a = round((self.b/self.a),2)
                if (center[0]<0) and (center[1]<0):
                    asymp_eq = f'(y+{center[1]})=±{b_over_a}(x+{center[0]})'
                elif (center[0]>0) and (center[1]<0):
                    asymp_eq = f'(y+{center[1]})=±{b_over_a}(x-{center[0]})'
                elif (center[0]<0) and (center[1]>0):
                    asymp_eq = f'(y-{center[1]})=±{b_over_a}(x+{center[0]})'
                else:
                    asymp_eq = f'(y-{center[1]})=±{b_over_a}(x-{center[0]})'

                information = f"CENTER{center}\nFOCUS1{focus1}\nFOCUS2{focus2}\nVERTEX1{vertex1}\nVERTEX2{vertex2}\nASYMPTOTE EQUATION:{asymp_eq}"
                self.result.setText(information)
            else:
                QMessageBox.warning(self, "Error", "The value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)

    def graphHyperbolaYmaj(self):
        try:
            if self.a > self.b:
                hyperbolaYmaj_object = HyperbolaYmaj(self.a,self.b,self.h,self.k)
                hyperbolaYmaj_object.graph_parts()
            else:
                QMessageBox.warning(self, "Error", "The value of A must be greater than B", QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.warning(self, "Error", "Press calculate before viewing the graph!", QMessageBox.Ok, QMessageBox.Ok)


class IdentifierWindow(QWidget): # Identifies the type of Conic Section
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conic Identifier")
        self.setWindowIcon(QIcon('sage'))
        self.setStyleSheet("background-color: rgb(166, 191, 200);")
        self.setGeometry(730,380,250,250)
        self.initUI()
    
    def initUI(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1,2)
        
        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.setLayout(self.hbox)
        self.list_of_textbox = []
        

        names = ('', 'x² +', '', 'xy+','','y²+','','x+','','y+','','=','0')

        # using a loop to generate positions
        for name in names:
            if name == '':
                self.textbox = QLineEdit(self)
                self.textbox.setPlaceholderText(name)
                self.textbox.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 12pt \"Arial\";")
                self.textbox.setFixedSize(30,20)
                self.list_of_textbox.append(self.textbox)
                self.hbox.addWidget(self.textbox)
            else:
                character = QLabel(name)
                self.hbox.addWidget(character)
        
        calculate_button = QPushButton("Identify!",self)
        calculate_button.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(85, 85, 255);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 13pt \"Permanent Marker\";")
        calculate_button.move(130,140)
        calculate_button.clicked.connect(self.identifierMethod)

    @pyqtSlot()
    def identifierMethod(self):
        try:
            A = int(self.list_of_textbox[0].text())
            B = int(self.list_of_textbox[1].text())
            C = int(self.list_of_textbox[2].text())
        except:
            QMessageBox.warning(self, "Error", "The value/s must be a numerical!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            
            discriminant = (B**2)-(4*A*C)   

            # Discriminant is a characteristic of a conic section. With it, the type can be determined
            if (discriminant<0) and ((B == 0) and (A == C)):
                QMessageBox.information(self, "Identified!", f"The equation has a type of CIRCLE which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            elif (discriminant<0) and ((B!=0) or (A!=C)):
                QMessageBox.information(self, "Identified!", f"The equation has a type of ELLIPSE which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            elif discriminant>0:
                QMessageBox.information(self, "Identified!", f"The equation has a type of HYPERBOLA which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            elif discriminant == 0:
                QMessageBox.information(self, "Identified!", f"The equation has a type of PARABOLA which has a determinant of {discriminant}", QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Error", "The equation is not a conic section!", QMessageBox.Ok, QMessageBox.Ok)
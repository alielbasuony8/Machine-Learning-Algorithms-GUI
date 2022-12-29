import warnings
# ignore all future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")


from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import linearRegression

class mainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "Linear regression application"
        self.top = 300
        self.left = 600
        self.width = 700
        self.height = 500
        self.iconName = "E:/ML project/asset/python.png"
        self.initUI()
        self.setStyleSheet('background-color: #023047; color: #fff; font-size: 25px')
        
        
    def initUI(self):               
        
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.drawBrowser()
        self.rftButton = self.createButton("Run",self.runlr,600, 430,80, 50).setStyleSheet('background-color: #fb8500; border-radius: 7px;')
        
        self.show()
        
        
        
    
    def drawBrowser(self):
        self.centralwidget = QWidget(self) 
        self.csv_label = QLabel(self.centralwidget) 
        self.csv_label.setGeometry(QtCore.QRect(10, 10, 120, 20))
        self.csv_label.setText("csv file: ")
        
        self.csv_lineEdit = QLineEdit(self)
        self.csv_lineEdit.setGeometry(QtCore.QRect(150,10,400,50))
        self.svmButton = self.createButton("Browse",self.getFileName,580, 10,100, 50).setStyleSheet('background-color: #219ebc; border-radius: 7px;')
        
    
    
    def getFileName(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Single File', 'E:\ML project\scripts' , '*.csv')
        self.csv_lineEdit.setText(fileName)
        self.fileName = self.csv_lineEdit.text()
        #print(self.fileName)

        
        
    
    def runlr(self):
        self.results = linearRegression.run(self.fileName)
        
        #QMessageBox.about(self,"Results:", self.results) 



    def createButton(self, text, fun, x, y, l, w):
        pushButton = QPushButton(text, self) 
        pushButton.setGeometry(QtCore.QRect(x, y, l, w))
        pushButton.clicked.connect(fun)
        return pushButton
        
        
def Main():
    m = mainWindow()
    m.show()
    return m
    
if __name__=="__main__":   
    import sys
    app = QApplication(sys.argv)
    mWin = mainWindow()
    sys.exit(app.exec_())
import warnings
# ignore all future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")


from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import svm

class mainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "SVM application"
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
        
        self.setDefault()        
        self.drawBrowser()
        self.drawSplit()                
        self.drawKernel()        
        
        self.svmButton = self.createButton("Run",self.runSVM,600, 430,80, 50).setStyleSheet('background-color: #fb8500; border-radius: 7px;')
        
        self.show()
        
        
    def setDefault(self):
        # self.fileName = ""
        self.splitSize = 20
        self.kernelType = 'rbf'
        
    
    def drawBrowser(self):
        self.centralwidget = QWidget(self) 
        self.csv_label = QLabel(self.centralwidget) 
        self.csv_label.setGeometry(QtCore.QRect(10, 10, 120, 20))
        self.csv_label.setText("csv file: ")
        
        self.csv_lineEdit = QLineEdit(self)
        self.csv_lineEdit.setGeometry(QtCore.QRect(150,10,400,50))
        self.svmButton = self.createButton("Browse",self.getFileName,580, 10,100, 50).setStyleSheet('background-color: #219ebc; border-radius: 7px;')
        
    
        
    def drawSplit(self):
        self.split_label = QLabel("test_data size(%): ",self)              
        self.split_label.setGeometry(QtCore.QRect(40,100, 200, 30))
        
        self.split_lineEdit = QLineEdit(self)
        self.split_lineEdit.setGeometry(QtCore.QRect(270,100,80,40))
        self.split_lineEdit.setStyleSheet('background-color: #fff;border-radius: 5px; color: #333 ')
        self.split_lineEdit.setText(str(self.splitSize))
        
    def drawKernel(self):
        self.kernel_label = QLabel("kernel type: ",self)
        self.kernel_label.setGeometry(QtCore.QRect(40,160, 200, 30))
        
        self.kernel_cb = QComboBox(self)
        self.kernel_cb.setGeometry(QtCore.QRect(270,160,100,40))
        self.kernel_cb.addItems(["rbf", "linear"])
        self.kernel_cb.setStyleSheet('background-color: #fff;border-radius: 5px; color: #333 ')
        self.kernel_cb.currentIndexChanged.connect(self.selectionChange)
        
    
        
    
    def selectionChange(self):
        # print (self.kernel_cb.currentText())
        self.kernelType = self.kernel_cb.currentText()
    
    def getFileName(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Single File', 'E:\ML project\scripts' , '*.csv')
        self.csv_lineEdit.setText(fileName)
        self.fileName = self.csv_lineEdit.text()
        #print(self.fileName)

    def runSVM(self):
        # print("--------TRAINING--------")
        if self.fileName != "":
            self.splitSize = int(self.split_lineEdit.text())
            self.kernelType = self.kernel_cb.currentText()
            if self.splitSize <=40:
                # print("test size =",self.splitSize,"%")
                # print("kernel:",self.kernelType)
                # print("degree:",self.degree)
                # print("tolerance value:",self.tol)
                # print("regularization parameter:",self.regParam)
                self.results = svm.run(self.fileName,self.splitSize,self.kernelType)
            else:
                pass# print("cannot train on such small dataset")
        else: 
            pass# print("incorrect file name!")            
        # print("--------SUCCESSFUL--------")
        

        

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
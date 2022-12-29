import warnings
# ignore all future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")


from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit,QHBoxLayout,QPushButton
import classificationRunner, regressionRunner


class mainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "ML Application"
        self.top = 150
        self.left = 500
        self.width = 1000
        self.height = 800
        self.iconName = "E:/ML project/asset/python.png"
        self.initUI()
        self.setStyleSheet('background-color: #e9c46a')
        
    def createButton(self,text,fun,x,y,l,w):
        pushButton = QPushButton(text,self) 
        pushButton.setGeometry(QtCore.QRect(x,y,l,w))
        pushButton.clicked.connect(fun)
        return pushButton    
                
    def initUI(self):               
        
        #self.title
        
        
        #self.statusBar().showMessage('Ready')
        
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.classificationButton = self.createButton("Classification",self.callClassificationRunner,300, 300,150, 100)
        self.classificationButton.setStyleSheet('background-color: #264653; color: #fff; font-size: 20px; border-radius: 5px;')
        self.regressionButton = self.createButton("Regression",self.callRegressionRunner,500, 300,150, 100)
        self.regressionButton.setStyleSheet('background-color: #264653; color: #fff; font-size: 20px; border-radius: 5px;')
        
        
        
        self.show()
        
        
    def callClassificationRunner(self): 
        self.m = classificationRunner.Main()
        
    def callRegressionRunner(self): 
        self.m = regressionRunner.Main()
    
if __name__=="__main__":   
    import sys
    app = QApplication(sys.argv)
    mWin = mainWindow()
    sys.exit(app.exec_())
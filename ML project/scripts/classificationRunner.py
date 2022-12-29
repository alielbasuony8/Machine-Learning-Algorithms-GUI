import warnings
# ignore all future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")


from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit,QHBoxLayout,QPushButton
import SVMRunner, DecisionTreeRunner, knnRunner, randomForestTreeRunner


class mainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = "Classification"
        self.top = 150
        self.left = 500
        self.width = 1000
        self.height = 800
        self.iconName = "C:/Users/user/Documents/pythonprog/ML/MLGUI/assets/python.png"
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

        self.svmButton = self.createButton("SVM",self.callSVMRunner,200, 300,100, 80).setStyleSheet('background-color: #264653; color: #fff; font-size: 20px; border-radius: 5px;')
        self.dtButton = self.createButton("Decision Tree",self.callDecesionTreeRunner,320, 300,130, 80).setStyleSheet('background-color: #264653; color: #fff; font-size: 20px; border-radius: 5px;')
        self.mlpButton = self.createButton("KNN",self.callknnRunner,470, 300,100, 80).setStyleSheet('background-color: #264653; color: #fff; font-size: 20px; border-radius: 5px;')
        self.rftButton = self.createButton("Random Forest tree",self.callRFTRunner,590, 300,190, 80).setStyleSheet('background-color: #264653; color: #fff; font-size: 20px; border-radius: 5px;')
        
        
        
        self.show()
        
        
    def callSVMRunner(self): 
        self.m = SVMRunner.Main()
        
    def callDecesionTreeRunner(self): 
        self.m = DecisionTreeRunner.Main()
    
    def callknnRunner(self): 
        self.m = knnRunner.Main()
    def callRFTRunner(self): 
        self.m = randomForestTreeRunner.Main()
        
        
if __name__=="__main__":   
    import sys
    app = QApplication(sys.argv)
    mWin = mainWindow()
    sys.exit(app.exec_())




def Main():
    m = mainWindow()
    m.show()
    return m
       
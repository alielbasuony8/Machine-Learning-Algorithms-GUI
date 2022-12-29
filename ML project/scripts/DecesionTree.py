import warnings
# ignore all future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from tkinter import *
from tkinter import messagebox
#import matplotlib.pyplot as plt
#from sklearn.metrics import plot_confusion_matrix



def run(file_name, testing_percentage):
    data = pd.read_csv(file_name)
    
    #df2 = df.reindex(np.random.permutation(df.index))
    #print(df)
    
    ts = (testing_percentage)/100
   

    x=data.iloc[:,:-1]
    y=data.iloc[:,-1]
    #print("X shape:",x.shape,"\nY shape",y.shape)
    #Y.ravel()
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=ts,random_state=109)
    
    sc_X = StandardScaler()
    x_train = sc_X.fit_transform(x_train)
    x_test = sc_X.transform(x_test)
    #print(X_train)
    #Y_train.ravel()
    clf = DecisionTreeClassifier()
    clf = clf.fit(x_train,y_train)
    
    y_pred = clf.predict(x_test)
    plt.figure(figsize=(12,12))
    tree.plot_tree(clf,fontsize=6)
    a = plt.show()



    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # 70% train 30% test
    model=DecisionTreeClassifier(criterion='entropy',max_depth=3)
    model=model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    plt.figure(figsize=(12,12))
    tree.plot_tree(model,fontsize=6)
    b = plt.show()

    
    window = Tk()
    window.title("Result")
    window.geometry("600x500")
    window.configure(bg='#023047')
    conf = Label(window,text= f"confusion matrix: {confusion_matrix(y_pred,y_test)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    conf.pack()
    accuracy = Label(window,text= f"Accuracy: {metrics.accuracy_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    accuracy.pack()
    precision = Label(window,text= f"precision: {metrics.precision_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    precision.pack()
    fOneScore = Label(window,text= f"f1-score: {metrics.f1_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    fOneScore.pack()
    recall = Label(window,text= f"Recall: {metrics.recall_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    recall.pack()
    window.mainloop()
    
    
    #results = classification_report(Y_test, Y_predict)
    # print(results)
    # print(clf.score(X_test, Y_test))
    #return results
#run('C:/Users/user/Documents/pythonprog/ML/MLGUI/scripts/bill_authentication.csv',20,'gini','best')

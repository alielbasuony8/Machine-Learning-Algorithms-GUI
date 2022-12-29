import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import seaborn as sns
from tkinter import *
from tkinter import messagebox

def run(file_name):
    data=pd.read_csv(file_name)
    print(data.shape)
    #print(data.head)
    x=data.iloc[:,:-1].values
    y=data.iloc[:,-1].values
    k=16
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # 70% train 30% test
    clf=KNeighborsClassifier(n_neighbors=k)
    clf=clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    conf = confusion_matrix(y_pred,y_test)
    error_rate=[]
    for i in range(1,40):
        knn=KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train,y_train)
        pred_i=knn.predict(X_test)
        error_rate.append(np.mean(pred_i!=y_test))

    plt.figure(figsize=(10,6))
    plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red',markersize=10)
    plt.title('ErrorRate vs. K-value')
    plt.xlabel('K')
    plt.ylabel('ErrorRate')
    plt.show()
    window = Tk()
    window.title("Result")
    window.geometry("600x500")
    window.configure(bg='#023047')
    conf = Label(window,text= f"confusion matrix: {conf}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    conf.pack()
    accuracy = Label(window,text= f"Accuracy: {metrics.accuracy_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    accuracy.pack()
    precision = Label(window,text= f"precision: {metrics.precision_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    precision.pack()
    fOneScore = Label(window,text= f"f1-score: {metrics.f1_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    fOneScore.pack()
    recall = Label(window,text= f"Recall: {metrics.recall_score(y_test, y_pred)}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    recall.pack()
    minumumError = Label(window,text= f"MinumError: {min(error_rate)} at k = {error_rate.index(min(error_rate))+1}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    minumumError.pack()
    window.mainloop()


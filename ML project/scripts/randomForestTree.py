#using kfold and fit rf classifier  and prdict the output
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from tkinter import *
def run(file_name,k_Fold):
    k=k_Fold
    #loading data
    data = pd.read_csv(file_name) #dataframe
    X=data.drop('outcome',1)
    y=data['outcome']
    rf = RandomForestClassifier(n_estimators = 10)
    kfold =KFold(n_splits=k, random_state=None, shuffle=False)
    acclist=[]
    for train_index, test_index in kfold.split(X):
        X_train , X_test = X.iloc[train_index,:],X.iloc[test_index,:]
        y_train , y_test = y[train_index] , y[test_index]
        rf.fit(X_train, y_train)
        predictions = rf.predict(X_test)
        from sklearn.metrics import confusion_matrix
        matrix = confusion_matrix(y_test, predictions)
        from sklearn.metrics import accuracy_score
        acc=accuracy_score(y_test,predictions)
        acclist.append(acc)
    
    acc = sum(acclist)/k
    print(acc)
    window = Tk()
    window.title("Result")
    window.geometry("600x500")
    window.configure(bg='#023047')
    acc= Label(window,text= f"Accuracy: {acc}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    acc.pack()
    window.mainloop()



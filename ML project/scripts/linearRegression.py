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

def run(file_name):
    data=pd.read_csv(file_name)
    print(data.shape)
    #print(data.head)
    x=data.iloc[:,:-1].values
    y=data.iloc[:,-1].values

    observation_count=51
    x_var=np.linspace(start=0,stop=10,num=observation_count)
    np.random.seed(22)
    y_var=x_var+np.random.normal(size=observation_count,loc=1,scale=2)
    sns.scatterplot(x=x_var,y=y_var)
    plt.show()


    X_train, X_test, y_train, y_test = train_test_split(x_var.reshape(-1,1),y_var, test_size=0.3,random_state=42) # 70% train 30% test
    linear_regress=LinearRegression()
    linear_regress.fit(X_train,y_train)
    predi=linear_regress.predict(X_test)
    rmse=mean_squared_error(predi,y_test)
    print(rmse)
    window = Tk()
    window.title("Result")
    window.geometry("600x500")
    window.configure(bg='#023047')
    acc= Label(window,text= f"Result: {rmse}",height=2,font=("Arial",20),bg='#023047',fg='#fff')
    acc.pack()
    window.mainloop()


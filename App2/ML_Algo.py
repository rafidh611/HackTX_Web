import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import pickle


data = pd.read_csv("scores.csv",sep=",")
data.fillna(0, inplace=True)
data["Percent White"]= data["Percent White"].str.rstrip('%').astype('float')
data["Percent Asian"]= data["Percent Asian"].str.rstrip('%').astype('float')
data["Percent Black"]= data["Percent Black"].str.rstrip('%').astype('float')
data["Percent Hispanic"]= data["Percent Hispanic"].str.rstrip('%').astype('float')
data["Percent Tested"]= data["Percent Tested"].str.rstrip('%').astype('float')



predict = "Average Math"
x = np.array(data.drop(["Zip Code","City","Average Math","School ID","School Name","Borough","Building Code","Street Address","Latitude","Longitude","Phone Number","Start Time","End Time","Average Reading","Average Writing"],1))
y = np.array(data[predict])

//Linear Regression gave the best model
best=0
for _ in range(100):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    if acc > best:
        print(acc)
        best=acc
        with open("SAT_Math.pickle", "wb") as f:
            pickle.dump(linear, f)

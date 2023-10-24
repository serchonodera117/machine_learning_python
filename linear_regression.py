# -*- coding: utf-8 -*-
#*
#Created on Tue Oct 24 12:42:15 2023
#simple linear regression 
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import requests as http
from sklearn.model_selection import train_test_split

data_url = "http://lib.stat.cmu.edu/datasets/boston"
httpdata = http.get(data_url)
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

print("data shape")
print(data.shape)
print("------------\n")


X = data[:, np.newaxis,5]
Y = target


plt.scatter(X,Y)
plt.xlabel("Num of rooms")
plt.ylabel("Average value")
plt.show()

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)
lr = linear_model.LinearRregression()
#train  model
lr.fit(x_train,y_train)

#prediction
Y_pred= lr.predict(x_test)


plt.scatter(x_test, y_test)
plt.plot(x_test, y_test, color='rded', linewidth=3)
plt.title("simple regression")
plt.xlabel("num of rooms")
plt.ylabel("Average value")
plt.show()
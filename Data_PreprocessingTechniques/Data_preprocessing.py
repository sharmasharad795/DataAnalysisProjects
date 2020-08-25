#Data pre-processing
#Importing libs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing the dataset
dataset=pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

#Taking care of missing data
from sklearn.preprocessing import Imputer 
#axis =0 is mean of cols..axis=1 is for rows
imputer=Imputer(missing_values='NaN',strategy = 'mean',axis=0)
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

#encoding categorical data
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
labelencoder_x=LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])

#countries get replaced by 0,1,2 but mL algos can interpret that as
# FRance being greater than Spain or something..
#hence we do separate encoding for each country category
onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()

#enoding 'purchase' col...here 0 and 1 refer to no/yes..so no need for
#OneHotEncoder
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)

#spliiting into training and test set
#train set on which we build ML model
#test set on which we test the perf of ML model
from sklearn.model_selection import train_test_split
#test_size=0.2 means 20% of data used for test case and rest for train case
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#feature scaling
#this is done to prevent numerical values difference affect ML models
#in this eg, age has comparatively smaller nos as salary,thus salary will have more say in eucleadian model
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)
#not applying f.scaling to dependent variable as it more of a binary classification



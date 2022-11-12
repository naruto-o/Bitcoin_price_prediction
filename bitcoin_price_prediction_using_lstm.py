# -*- coding: utf-8 -*-
"""Bitcoin_price_prediction_using_lstm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fm6AJQmzq7wPlU4fgWAGt3d_R6SH8uwQ
"""

!pip install pandas
!pip install numpy
! pip install matplotlib
! pip install sklearn
!pip install tensorflow

# importing the necessary libraries
import os 
import io
import pandas as pd
import numpy as np
import math 
import datetime as dt
import matplotlib.pyplot as plt

# for evaluation we will use these libraries
from sklearn.metrics import mean_squared_error,mean_absolute_error,explained_variance_score,r2_score
from sklearn.metrics import mean_poisson_deviance,mean_gamma_deviance,accuracy_score
from sklearn.preprocessing import MinMaxScaler

# for model building we will use these libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.layers import LSTM

# for plotting we will use these library
import matplotlib.pyplot as plt
from itertools import cycle
import plotly.graph_objects as go
import  plotly.express as px
from plotly.subplots import make_subplots

# loading dataset

# load our dataset
# i have downloaded my dataset from yahoo finance of bitcoin in a csv file
maindf = pd.read_csv('/content/BTC-USD.csv')
print('Total number of days present in the dataset: ',maindf.shape[0])
print('Total number of fields present in the dataset: ',maindf.shape[1])

maindf.shape

maindf.head()

maindf.tail()

maindf.info()

maindf.describe()

# checking for null values
print('Null Values:',maindf.isnull().values.sum())
print('NA values:',maindf.isnull().values.any())
maindf.shape

# Exploratory data analysis
# print the start date and end date of the datset
sd = maindf.iloc[0][0]
ed = maindf.iloc[-1][0]

print('Starting date',sd)
print('Ending date',ed)

# Stock price analysis from start
# analysis of year 2014
maindf['Date'] = pd.to_datetime(maindf['Date'],format = '%Y-%m-%d')
y_2014 = maindf.loc[(maindf['Date']>='2014-09-17') & (maindf['Date'] < '2014-12-31')]
y_2014.drop(y_2014[['Adj Close','Volume']],axis=1)

monthvise= y_2014.groupby(y_2014['Date'].dt.strftime('%B'))[['Open','Close']].mean()
new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
             'September', 'October', 'November', 'December']
# by using reindex() method and by specifying the axis we want to reindex. Default values in the new index that are not present in the dataframe are assigned NaN
monthvise = monthvise.reindex(new_order, axis=0)
monthvise
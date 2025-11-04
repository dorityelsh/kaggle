# Supress Warnings

import warnings
warnings.filterwarnings('ignore')

# Import the numpy and pandas package

import numpy as np
import pandas as pd

# Data Visualisation

import matplotlib.pyplot as plt  
import seaborn as sns

housing = pd.DataFrame(pd.read_csv("/Users/idan/Documents/Housing.csv"))

# Data Inspection
print (housing.head())
print(housing.shape)
print (housing.info())
print (housing.describe())

print(housing.isnull().sum()*100/housing.shape[0])

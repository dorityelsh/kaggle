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
# print(housing.shape)
# print (housing.info())
# print (housing.describe())

# print(housing.isnull().sum()*100/housing.shape[0])5
# fig, axs = plt.subplots(2,3, figsize = (10,5))
# plt1 = sns.boxplot(housing['price'], ax = axs[0,0])
# plt2 = sns.boxplot(housing['area'], ax = axs[0,1])
# plt3 = sns.boxplot(housing['bedrooms'], ax = axs[0,2])
# plt1 = sns.boxplot(housing['bathrooms'], ax = axs[1,0])
# plt2 = sns.boxplot(housing['stories'], ax = axs[1,1])
# plt3 = sns.boxplot(housing['parking'], ax = axs[1,2])

# plt.tight_layout()

# plt.show()
# sns.pairplot(housing)
# plt.show()
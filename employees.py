# -*- coding: utf-8 -*-
"""Employees

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1igRV5_OZ4yQmjUWSgvgtzt5h9Uq4pYZJ
"""

# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import pickle as pickle
import os

new_var = pd.read_excel("/content/employee_burnout_analysis 2-AI.xlsx")
data = new_var

data.nunique()

data.info()

data.isnull().sum()

data.isnull().sum().values.sum()

data.corr(numeric_only=True)['Burn Rate'][:-1]

"""## Exploratory Data Analysis

# New Section

These two variables are strongly correlated with target variable, therefore , important to estimate it.
"""

sns.pairplot(data)
plt.show()

"""Drop off all observations with NaN values of our dataframe."""

data = data.dropna()

data.shape

data.shape



"""Analyzing what type of data is each variable."""

data.dtypes

data.dtypes

""" The values that each variable contains."""

data_obj = data.select_dtypes(object)
# prints a dictionary of max 10 unique values for each non-numeric column
print({ c : data_obj[c].unique()[:10] for c in data_obj.columns})

"""

```
# This is formatted as code
```

 The employees ID doesn't provide any useful information and, therefore, they must be dropped."""

data = data.drop('Employee ID', axis = 1)

"""data.head()

Checking the correlation of Date of Joining with Target variable
"""

print(f"Min date {data['Date of Joining'].min()}")
print(f"Max date {data['Date of Joining'].max()}")
data_month = data.copy()

data_month["Date of Joining"] = data_month['Date of Joining'].astype("datetime64[ns]")
data_month["Date of Joining"].groupby(
    data_month['Date of Joining'].dt.month
).count().plot(kind="bar", xlabel='Month', ylabel="Hired employees")

""" The date of joining is uniform distributed with values between 2008-01-01 and 2008-12-31. So in order to create a new feature which represents the labor seniority, we could create a variable with de days worked"""

data_2008 = pd.to_datetime(["2008-01-01"]*len(data))
data["Days"] = data['Date of Joining'].astype("datetime64[ns]").sub(data_2008).dt.days
data.Days

data.corr(numeric_only=True)['Burn Rate'][:]









"""We observed that there is no strong correlation between Date of Joining and Burn Rate.So, we are dropping the column Date of Joining."""

data = data.drop(['Date of Joining','Days'], axis = 1)

data.head()

"""Now  analysing the categorical variables"""

cat_columns = data.select_dtypes(object).columns
fig, ax = plt.subplots(nrows=1, ncols=len(cat_columns), sharey=True, figsize=(10, 5))
for i, c in enumerate(cat_columns):
    sns.countplot(x=c, data=data, ax=ax[i])
plt.show()



"""The number of observations of each category on each variable is equally distributed, except to the Company_Type where the number of service jobs its almost twice that of product ones.

"""

data.columns

data = pd.get_dummies(data, columns=['Company Type', 'WFH Setup Available',
       'Gender'], drop_first=True)
data.head()
encoded_columns = data.columns
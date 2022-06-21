# Wicaksa Munajat
# CST 383 Summer '22
# 05/16/2022
# Lab: Data: Missing (20 min)


#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('paper') # 'talk' for slightly larger

# change default plot size
rcParams['figure.figsize'] = 9,7


# Instructions
#
# In this lab we'll practice treating NA values in Pandas.  Remember, in Pandas both None and nan values are thought of as NA values.
#
# We’ll start with data on air quality in New York City in 1973. Here is a link:
# https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv (Links to an external site.)
# (source of data: 'airquality' data set supplied with R programming language)

# #### 1. Read the data as a Pandas data frame as variable 'df'.

# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv")


# #### 2. Display the first rows of the data frame in the console

# In[3]:


df.head()


# #### 3. What are the types of columns in the data frame?  Write the code to display them.

# In[4]:


df.columns
# output: Index(['Ozone', 'Solar_R', 'Wind', 'Temp', 'Month', 'Day'], dtype='object')


# #### 4. What is the total number of NA values in the data frame?  What fraction of all the values in the data frame are NA's?

# In[5]:


# total number of NaN values
df.isna().sum().sum() # total = 44 (Ozone has 37 and Solar_R has 7)
# total number of values
df.count().sum() # 874
# fraction of NaN / total values
np.divide(df.isna().sum().sum(), df.count().sum())


# #### 5. How many rows contain NA values?

# In[6]:


df.isnull().any(axis=1).sum() # 42 Rows


# #### 6. For each column, what fraction of the column values are NA values?

# In[7]:


# find number of rows
len(df.index) # 153

# find out how many NaN values in each column
df.isna().sum()
"""
Output:
Ozone      37
Solar_R     7
Wind        0
Temp        0
Month       0
Day         0
dtype: int64
"""

# Ozone Column : 37/153
# Solar_r : 7/153
# Rest : 0/153


# #### 7. For each row, what fraction of the row values are NA?

# In[ ]:





# #### 8. Following problem 6, plot, for each column, the fraction of the values in that column that are NA.

# In[8]:


x = df.columns
y = [37/153, 7/153, 0, 0, 0, 0]

plt.bar(x,y)


# #### 9. In this data set, if you decided to remove the NA values, would you do it by removing rows, or by removing columns?

# In[9]:


# I would remove rows. This will give a more complete picture with the rest of the data since most of them still have Ozone and Solar_R Values.


# #### 10. Create a new data frame df_cleanrows that is like dat except all rows containing NA values are removed.  Verify that there are no NA values in df_cleanrows.

# In[10]:


df_cleanrows = df.dropna(axis=0) # axi 0 = rows
df_cleanrows


# #### 11. Create a new data frame df_cleancols that is like dat except all columns containing NA values are removed.

# In[11]:


df_cleancols = df.dropna(axis=1) # axis 1 = cols
df_cleancols


# #### 12. Which contains more data, df_cleanrows, or df_cleancols?

# In[12]:


# df_cleancols has 153 rows x 4 columns
# df_cleanrows has 111 rows x 6 colums


# #### 13. Create a new data frame df_med from your original data frame ‘df’ by replacing each NA value with the median of its column.

# In[13]:


# create new df
df_med = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv")

# Using median in 'Ozone' to replace NaN
df_med['Ozone'].fillna(df_med['Ozone'].median(), inplace=True)

# Using median in 'Solar_R' to replace NaN
df_med['Solar_R'].fillna(df_med['Solar_R'].median(), inplace=True)

df_med # 153 rows × 6 columns


# #### 14. Create a new data frame df_mean from your original data frame ‘df’ by replacing each NA value with the mean of its column.

# In[14]:


# create new df
df_mean = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv")

# Using mean in 'Ozone' to replace NaN
df_mean['Ozone'].fillna(df_mean['Ozone'].mean(), inplace=True)

# Using mean in 'Solar_R' to replace NaN
df_mean['Solar_R'].fillna(df_mean['Solar_R'].mean(), inplace=True)

df_mean # 153 rows × 6 columns


# #### 15. If you still have time, write code to handle missing values in the Iris dataset as described at the end of the lecture.
#
# Here is a URL for the Iris dataset used in the lecture.
# https://raw.githubusercontent.com/grbruns/cst383/master/iris-na.csv

#!/usr/bin/env python
# coding: utf-8

# # -*- coding: utf-8 -*-
# """
# Pandas dataframes
# @author: Glenn Bruns
# """
# import numpy as np
# import pandas as pd

# In[1]:


import numpy as np 
import pandas as pd


# Allow output to span multiple output lines in the console.

# In[2]:


pd.set_option('display.max_columns', 500)


# =============================================================================<br>
# Read data<br>
# =============================================================================

# Read 1994 census summary data.

# In[3]:


df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv")
df.set_index('usid', inplace=True)
df.drop('fnlwgt', axis=1, inplace=True)


# =============================================================================<br>
# Simple aggregation<br>
# =============================================================================

# Print the average age.

# In[4]:


print(df['age'].mean())


# Get the min, max, and avg value for each numeric column. <br>
# For a dataframe you get the aggregate for each column by default.

# In[5]:


df.aggregate(['min', 'max', 'mean'])


# =============================================================================<br>
# Aggregation with grouping<br>
# =============================================================================

# How many people in each category of education?<br>
# Try using pandas function value_counts().

# In[6]:


df['education'].value_counts()


# For each native country, what is the average education num?

# In[7]:


df['native_country'].value_counts()


# In[8]:


# Split, apply function, combine

# You can also filter 
# filt = df['native_country'] == "United_States"
# df.loc[filt]

# Split, group by country & save it to variable
country_group = df.groupby(['native_country']) # list of columns you want to group by

# Get the mean for the education_num
country_group['education_num'].mean()


# Repeat the previous problem, sorting the output by the average education num value. <br>
# 
# DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)[source] <br>
# 
# df.sort_values(by=['col1'])

# In[9]:


country_group['education_num'].mean().sort_values(ascending=False)


# For each occupation, compute the median age.

# In[10]:


df.head(10)
# Store df w/ occupation into a variable
occ_group = df.groupby(['occupation'])

# Compute the median age of the group
occ_group['age'].median()


# Repeat the previous problem, but sort the output.

# In[11]:


occ_group['age'].median().sort_values(ascending=True)


# Find average hours_per_week for those with age <= 40, and those with age > 40<br>
# (this uses something labeled 'advanced' in the lecture).

# In[48]:


df.groupby(df['age']<= 40).mean()
df.groupby(df['age'] > 40).mean()


# Do the same, but for age groups < 40, 40-60, and > 60.

# In[53]:


print(df.loc[df['age'] < 40]['hours_per_week'].mean())
print(df.loc[df['age'] > 60]['hours_per_week'].mean())


# Get the rows of the data frame, but only for occupations
# with an average number of education_num > 10. (Hint: use filter.)

# In[60]:


df.head()
#You can also filter 
filt = df['education_num'] > 10
df.loc[filt]


# =============================================================================<br>
# Vectorized string operations<br>
# =============================================================================

# Create a Pandas series containing the values in the native_country column. Name this series 'country'.

# In[75]:


# You can convert Pandas DataFrame to a Series using squeeze: df.squeeze()
country = df['native_country'].squeeze()
print(country)


# How many different values appear in the country series? 32561

# Create a Series containing the unique country names in the series.<br>
# Name this new series 'country_names'.

# In[78]:


country_names = pd.Series(df['native_country'].unique())


# Modify country_names so that underscore '_' is replaced
# by a hyphen '-' in every country name.  Use a vectorized operation.<br>
# (See https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)

# In[79]:


# (1) Replace character/s under a single DataFrame column:
# df['column name'] = df['column name'].str.replace('old character','new character)

# (2) Replace character/s under the entire DataFrame:
# df = df.replace('old character','new character', regex=True)
country_names.str.replace('_', '-')


# Modify country_names to replace 'Holand' with 'Holland'.

# In[80]:


country_names.str.replace('Holand', 'Holland')


# Modify country_names so that any characters after 5 are removed.<br>
# Again, use a vectorized operation.

# In[81]:


country_names.str[0:4]


# Suppose we were to use only the first two letters of each country.<br>
# Write some code to determine if any two countries would then share<br>
# a name.

# In[ ]:





# If you still have time, write code to determine which countries<br>
# do not have a unique name when only the first two characters are<br>
# used.  Hint: look into Pandas' Series.duplicated().

# In[ ]:





# =============================================================================<br>
# Handling times and dates<br>
# =============================================================================

# read gas prices data

# In[ ]:


gas = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/Gasoline_Retail_Prices_Weekly_Average_by_Region__Beginning_2007.csv")


# create a datetime series and make it the index of the dataset

# In[ ]:





# plot the gas prices for NY city

# In[ ]:





# plot gas prices for NY city and Albany on the same plot

# In[ ]:





# if you still have time, see if you can find and plot California<br>
# gas prices

# In[ ]:





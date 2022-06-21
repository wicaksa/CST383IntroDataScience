#!/usr/bin/env python
# coding: utf-8

# # -*- coding: utf-8 -*-
# """
# Pandas dataframes lab
# Fill in your code after each comment (unless code already provided).
# @author: Glenn Bruns
# """

# In[1]:


import numpy as np
import pandas as pd


# Here are the names of seven CSUMB students.

# In[2]:


students = ['Sean', 'Laura', 'Angel', 'Mariana', 'Austin', 'Jose', 'Ana']


# Here are the MPG values for the students' cars.

# In[3]:


student_mileage = [21.1, 26.6, 16.3, 33.7, 31.2, 52.0, 27.1]


# create a Pandas dataframe df containing the MPG values, using the<br>
# names for the index.  Use 'mpg' for the mileage column.

# In[4]:


df = pd.DataFrame({'MPG': student_mileage}, index=students)


# print the dataframe you just created

# In[5]:


print(df)


# using df, print the mileage for Ana's car using the .loc attribute

# In[6]:


# Prints Sean
# df.loc[ROW #, 'Students']
# print(df.loc[0, 'Students'])
# Print Ana mpg
print(df.loc['Sean', 'MPG'])


# using df, print the rows of the dataframe where mpg > 30 (use a boolean mask)

# In[7]:


# To select rows whose column value equals a scalar, some_value, 
# use ==:
print(df.loc[df['MPG'] > 30.0])


# using df, print the mileage values for Laura and Austin using .loc

# In[8]:


print(df.loc['Laura', 'MPG'])
print(df.loc['Austin', 'MPG'])


# here are distances the students travel to get to CSUMB

# In[9]:


student_dist = {'Sean':8.1, 'Laura':5.4, 'Angel':12.8, 'Austin':15.0, 'Jose':22.2, 'Ana':18.5}


# create another dataframe df2 containing the distance values, and<br>
# again use the names for the index.  Use 'distance' for the<br>
# distance column.

# In[10]:


df2 = pd.DataFrame( {'Distance' : student_dist.values()}, index=student_dist.keys() )
print(df2)


# print the dataframe you get by adding 'distance' as a new column.  <br>
# All students should appear (Mariana will have NaN for distance).<br>
# Use pandas.join

# In[11]:


print(df.join(df2))


# update df using your last answer so that it includes the 'distance' column

# In[12]:


df = df.join(df2)
print(df)


# the distance value for Mariana should be 'NaN'.  Update the value<br>
# to 3.5 miles using .loc

# In[13]:


# https://stackoverflow.com/questions/42449169/overwriting-nan-values-with-loc-in-pandas
df.loc[np.isnan(df['Distance']), "Distance"] = 3.5
print(df)


# using df, show mpg and distance for students with distance > 20<br>
# Don't use .loc or .iloc

# In[14]:


df[ df['Distance'] > 20.0]


# repeat, but using .loc

# In[15]:


df.loc[df['Distance'] > 20]


# print the underlying 2D numpy array containing the dataframe data<br>
# (Hint: you use .index on a data frame to get the row index; how do<br>
# you get the data?)

# In[16]:


df.to_numpy()


# add a new column, 'gas', which shows the number of<br>
# gallons of gas needed for a round-trip drive to CSUMB

# In[17]:


# Create a new DataFrame
gas = pd.DataFrame( {'RoundTrip': student_dist.values()},
                      index = student_dist.keys())
# Multiply by 2 to get round trip values
gas = gas.multiply(2)
# Join to df table
df = df.join(gas)
df.loc[np.isnan(df['RoundTrip']), "RoundTrip"] = 7.0
print(df)


# print the first two rows of the data frame using .iloc

# In[18]:


# print(df.iloc[0]) #== prints first row 
# print(df.iloc[0,1]) # prints row 0, col 1
print(df.iloc[0:2])


# If you still have time, redo the problem above that asks you<br>
# to use pandas.join, but this time use pandas.merge.  You<br>
# will want to rerun your earlier code so that df has no<br>
# 'distance' column

# In[ ]:





# Repeat the problem you just solved, but use pandas.concat

# In[ ]:





# If you still have time, play more with some Pandas dataframes<br>
# to get comfortable with indexing.  Also, play with other<br>
# dataframe features discussed in lecture.

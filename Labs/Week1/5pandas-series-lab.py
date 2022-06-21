#!/usr/bin/env python
# coding: utf-8

# # -*- coding: utf-8 -*-
# """
# Pandas series lab
# @author: Glenn Bruns
# """

# In[6]:


import numpy as np
import pandas as pd


# Here are the MPG values for 7 students in a NumPy array.

# In[7]:


student_mileage = np.array([21.1, 26.6, 16.3, 33.7, 31.2, 52.0, 27.1])
print(student_mileage)


# Here are the names of the seven students.

# In[8]:


students = ['Sean', 'Laura', 'Angel', 'Mariana', 'Austin', 'Jose', 'Ana']


# Create a Pandas series containing the MPG values, using the names for the index.  Use variable 'mpg'.

# In[9]:


mpg = pd.Series(data=student_mileage, index=students)


# print the series you just created

# In[10]:


print(mpg)


# print the mileage for Ana's car using dictionary-style indexing

# In[12]:


print(mpg['Ana'])


# print the mileage for Mariana's car using 'loc'

# In[15]:


mpg.loc['Mariana']


# print the mpg values that are greater than 30.0<br>
# hint: use a boolean mask

# In[20]:


print(mpg[mpg > 30.0])


# create a series high_mpg that contains the mpg values<br>
# greater than 30.0

# In[21]:


high_mpg = pd.Series(mpg[mpg>30.0])


# print the high_mpg series

# In[33]:


print(high_mpg)


# print the names of the students who have cars with mpg
# greater than 30.0. 
# hint: what's in the index of high_mpg?

# In[38]:


print(high_mpg.index)


# create a NumPy array x from the data values in series mpg

# In[39]:


x = np.array(mpg)


# write code to make sure that x is really a numpy array,<br>
# and not just a Python list

# In[46]:


x = np.array(mpg)


# here are the distances that students have to travel (one-way)<br>
# to get to CSUMB

# In[47]:


student_dist = {'Sean':8.1, 'Laura':5.4, 'Angel':12.8, 'Austin':15.0, 'Jose':22.2, 'Ana':18.5}


# create a Pandas series 'distance' that gives the distance for each student

# In[48]:


distance = pd.Series(student_dist)


# create a series 'rt_distance' from 'distance' that gives the round-trip distance<br>
# hint: use a vectorized operation

# In[61]:


rt_distance = pd.Series(distance * 2)
rt_distance
# Sean       21.1
# Laura      26.6
# Angel      16.3
# Mariana    33.7
# Austin     31.2
# Jose       52.0
# Ana        27.1


# write code to see if the rt_distance series, and the mpg series, mention<br>
# the same students<br>
# hint: index objects support an 'equals' method

# In[58]:


# Check if the two keys/indexes are equal
mpg.keys().equals(rt_distance.keys())


# compute the gallons used in each CSUMB commute for each student by 
# dividing the round-trip distance values by the mpg values

# In[63]:


gallons_used = pd.Series(data=rt_distance/mpg, index=students)
print(gallons_used)


# repeat your calculation, but now give a value of 0 for students that<br>
# students not represented in the mpg or rt_distance time series

# In[64]:


gallons_used = pd.Series(data=rt_distance/mpg, index=students).fillna(0)
print(gallons_used)


# If you still have time, play more with some Pandas series<br>
# to get comfortable with indexing.  Also, play with other<br>
# series features discussed in lecture.

# Also, check out this "10 Minutes to pandas" tutorial:<br>
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

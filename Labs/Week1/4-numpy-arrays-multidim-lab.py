#!/usr/bin/env python
# coding: utf-8

# # -*- coding: utf-8 -*-
# Multidimensional NumPy arrays lab
# Enter your Python code after each prompt.
# @author: Glenn Bruns
# @student: Wicaksa Munajat

# In[8]:


import random
import numpy as np
import pandas as pd


# Read student exam score data as a 2D NumPy array.

# In[54]:


df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/sample-grades.csv").values
df = np.array(df)


# Print the score for the first student (row 0) and the third problem (column 2).

# In[72]:


print(df[0,2])


# Print all scores for student 15 (meaning row 15).

# In[63]:


print(df[14])


# Print all scores for problems 0-3.

# In[64]:


print(df[:,[0,1,2,3]])


# Print all scores for problems 1, 5, 7.

# In[65]:


print(df[:,[1,5,7]])


# Assign the number of students to variable 'num_students'.

# In[67]:


num_students = len(df)
#print(num_students)


# Run the following command to get random data representing scores
# on two additional extra credit problems.

# In[60]:


ec = np.random.choice(np.array([0,1,2,3], dtype='int64'), size=num_students*2).reshape(num_students, 2)


# Print the shape of ec.

# In[61]:


print(ec.shape)


# Update df so that the two rightmost columns are the data in array ec.

# In[80]:


df = np.hstack([df,ec])
# np.concatenate([df, np.array([[1], [1]]).dot(ec)], axis = 1)


# Print the mean value of all the scores.

# In[85]:


print(df.mean())


# Print the number of scores > 2  (np.sum applied to a boolean mask will give the number of True values in the mask)).

# In[97]:


print(np.sum(df > 2))
# or print((df > 2).sum())


# Using a list comprehension, compute the total score for each student
# and assign the result to variable 'totals' as a NumPy array.

# In[112]:


totals = np.array([sum(x) for x in df])
print(totals)


# Print the dtype of totals; it should be int64.

# In[113]:


print(totals.dtype)


# Assign the number of columns to variable 'num_problems'.

# In[114]:


num_problems = len(df)
print(num_problems)


# Using a list comprehension, compute the average score for each
# problem and assign the result to variable 'prob_means' as a NumPy array.

# In[119]:


prob_means = np.array([(sum(i)/num_problems) for i in zip(*df)])
print(prob_means)


# What is the lowest of the average score values?

# In[120]:


print(prob_means.min())


# Is it legal to subtract an array with shape (35,) from an
# array with shape (50,35)?  If so, what will happen?  Write
# your answer as a comment.

# In[121]:


# No.
# The array (35,) will become (1,35), and will be subtracted
# from each row of the (50,35) array


# Compute a new array df_centered, which is a 2D array with
# the same shape as df, but contains, for each column, the
# column values minus the average value for each column.

# In[143]:


# Sum of columns as 2D array.
df_centered = np.array([sum(i) for i in zip(*df)])
# Difference b/w each column - mean from each column
df_centered = np.subtract(df_centered, prob_means)


# What do you expect as the average values of the columns of<br>
# dat_centered?  Print the result to find out.

# In[144]:


print(df_centered)


# consider extending idea about length of student trips, but make a matrix,<br>
# where each row is a student, and 'mpg', 'miles' are columns.  In a separate<br>
# array, show prices of gas at several gas stations.

# In[ ]:

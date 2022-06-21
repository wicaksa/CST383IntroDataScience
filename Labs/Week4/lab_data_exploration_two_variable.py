
"""
Wicaksa Munajat
CST383 Summer 2022
05/20/2022

"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# The purpose of this lab is to give you experience in exploring data.  
# It is vital that develop the ability to explore the data on your own.  
# Leverage your curiosity!


# In[10]:


#@1. We’ll look at the US News and World Report college data.  The URL is:
url = 'https://raw.githubusercontent.com/grbruns/cst383/master/College.csv'


# In[12]:


#@2. The data is in CSV format.  Create a Python file in Spyder, and write code to load the data.  For example:
df = pd.read_csv(url, index_col=0) # use the 'index_col=0'
#  Record your work on the following problems in a Python file.


# In[16]:


#@3. Create scatter plots to compare some of the variables.  
#### Here are some questions to help you get started.  Follow your curiosity.
df.head()


# In[18]:


#### Do smaller colleges spend more?  (variables F.Undergrad and Expend)
#### It looks like smaller colleges spend more money than larger schools. 
sns.scatterplot(x='F.Undergrad', y='Expend', data=df)


# In[19]:


#### Do smaller colleges charge more?  (variables F.Undergrad and Outstate)
#### Smaller schools look like they charge a lot more than larger schools. 
sns.scatterplot(x='F.Undergrad', y='Outstate', data=df)


# In[32]:


#### Define two new variables: perc.accept and perc.enroll.  
#### The first is the percentage of students who accepted out of those who applied (use variables Accept and Apps).  
#### The second is the percentage of students who enrolled out of those where were accepted (use variables Enroll and Accept).
accept = np.divide(df['Accept'].sum(),df['Apps'].sum()) # 0.6725674910269939
enroll = np.divide(df['Enroll'].sum(),df['Accept'].sum()) # 38635391438667716


# In[ ]:


#@ 4. Think of more questions and see if you can create plots to help understand them.  
#### For example, are more selective colleges more expensive?  
#### Just create more scatterplots and explore them.  
#### There are lots of things to pursue in the college data.


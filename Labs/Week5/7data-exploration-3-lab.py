#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[1]:


#1.	We will continue with the college data set.
# https://raw.githubusercontent.com/grbruns/cst383/master/College.csv


# In[2]:


#2. Write code to load the data. For example:


# In[5]:


df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col = 0)


# In[6]:


# 3. Derive a new column, ‘Size’, from the F.Undergrad variable.  
# The possible values of Size should be “small”, “medium”, or “large”.   
# The value “small” should be assigned to the colleges in the “bottom 3rd” of F.Undergrad values, “medium” should be assigned to the “middle 3rd”, and “large” to the “top 3rd”.  
# Use the Pandas ‘quantile’ function to find the corresponding F.Undergrad values.  (If you're not sure how to do this, see the hints right away).


# In[8]:


df['F.Undergrad']


# In[14]:


# Split the data into different quantiles (0-33, 33-66, 66-100)
size = df['F.Undergrad'].quantile([0,0.33, 0.66, 1.0])

# Create a new column and assign them sizes according to their F.Undergrad values.
df['Size'] = pd.cut(df['F.Undergrad'],
                    include_lowest=True, 
                    bins=size,
                    labels=['small', 'medium', 'large'])


# In[15]:


# Create a barplot to make sure the number of small, medium, and large values are about the same.  
# When you make a quick plot for yourself, no need for adding a title or axis labels.  
# When you make a plot for a report or to share, it's important to use a good title and axis labels.


# In[23]:


df.Size.value_counts().plot.bar()


# In[24]:


#4.	Use the faceting (also known as 'conditioning') idea to create three scatter plots, one for each value of your new variable size.  
# The scatterplot should show PhD on the x axis and Outstate on the y axis.  
# Try to make your plot look approximately like this:


# In[26]:


g = sns.FacetGrid(df, col='Size', height=4, aspect=0.8)
g.map(plt.scatter, 'PhD', 'Outstate', s=20, color="r")


# In[27]:


# Look at the plots for a while and think their significance.   
# Is the plot for large colleges different from the plot for small colleges?  
# What does this say about large and small colleges. 
# Also, do you see any interesting outliers?


# In[28]:


# 5. Repeat problem 5, but this time show a single scatterplot, with color used to distinguish small, medium, and large schools.  
# Your plot might look something like this:


# In[29]:


# Look at the plot you created for this problem compared to the last problem.  
# Which do you think is easier to interpret.   
# Spend some time on this -- it's important.

# This plot is easier because it has every dot in one graph.


# In[30]:


sns.scatterplot(x='PhD', y='Outstate', hue='Size', data=df, s=50)


# In[31]:


# 6.Repeat the last plot, but this time use both shape and color to indicate college size.  
# Do you think your new plot is easier to interpret than your plot of the previous problem?
# It looks worse.


# In[32]:


sns.scatterplot(x='PhD', y='Outstate', hue='Size', style='Size', data=df, s=55)


# In[34]:


# 7. Create three violin plots, showing the distribution of tuition at each of the three college size values. 


# In[35]:


sns.catplot(y='Outstate', col='Size', data=df, kind='violin', height=4, aspect=0.7)


# In[36]:


# 8. Repeat the last plot, but now show the raw data on the plot.


# In[37]:


sns.catplot(y='Outstate', col='Size', data=df, kind='violin', inner='stick', height=4, aspect=0.7)


# In[38]:


# 9. If you still have time, repeat problem 4, but this time show 3 histograms of the PhD variable, one each for small, medium, and large schools.  
# Show the three histograms in a single column of plots.  


# In[40]:


g = sns.FacetGrid(df, row='Size', height=2.5, aspect=1.8)
g.map(plt.hist, 'PhD', color="b")


# In[ ]:





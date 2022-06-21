#!/usr/bin/env python
# coding: utf-8

# # -*- coding: utf-8 -*-
# """
# Python graphics lab
# @author: Glenn Bruns
# """

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams


# Change default plot size.

# In[3]:


rcParams['figure.figsize'] = 6,4
# change plotting style
plt.style.use('seaborn')


# =============================================================================<br>
# Read the 'mtcars' (Motor Trend cars) dataset<br>
# =============================================================================

# In[4]:


df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/mtcars.csv")


# =============================================================================<br>
# Plotting<br>
# =============================================================================

# Write Python code to answer the following questions.  Try hard to answer<br>
# the questions from memory before using the lecture slides or other resources.

# It takes practice to create good-looking plots.  It's a good idea to start<br>
# with a simple plot and then to improve it if the it appears useful.

# First, look at the mtcars data in Spyder, and using df.info(), to get an<br>
# idea of what is in the data set.  Some information about the data can be<br>
# found here:<br>
# https://www.rdocumentation.org/packages/datasets/versions/3.6.0/topics/mtcars

# (YOUR CODE HERE -- and similarly for further questions)

# In[44]:


df.head()


# Create a basic scatterplot showing each car’s mpg as a function of engine <br>
# displacement.  (in other words, mpg goes on the y axis and displacement on <br>
# the x axis.)  Use the matplotlib scatter() function.

# In[13]:


plt.scatter(df['disp'],df['mpg'])


# Improve your plot by adding 'displacement (cu. inches)' as the x axis<br>
# label, and 'miles per gallon' as the y axis label.

# In[19]:


# Create scatter plot
plt.scatter(df['disp'],df['mpg'])

# Add labels
plt.xlabel('miles per gallon')
plt.ylabel('cu. inches')
plt.show()


# Make the dots dark red.

# In[16]:


plt.scatter(df['disp'],df['mpg'],c="red")


# Use upward triangles instead of circles. (hint: use the 'marker' option in plt.scatter)

# In[18]:


plt.scatter(df['disp'],df['mpg'],marker="^")


# Add a title.<br>
# Hint: in scatter plats, we often say 'A by B' when A is the
# thing on the y axis and B is the thing on the x axis. For example: 'MPG by engine displacement'.

# In[20]:


# Create scatter plot
plt.scatter(df['disp'],df['mpg'])
# Add title 
plt.title('Car MPG as a Function of Engine Displacement')


# Compute the average mpg, and add a black dotted horizontal<br>
# line to show this value.

# In[42]:


# Compute the average mpg
avgMPG = df['mpg'].mean()
print(f"avgMPG = {avgMPG}")

# Create scatter plot
plt.scatter(df['disp'],df['mpg'], c="red", label="mpg_disp")

# Plot horizontal dotted line
plt.axhline(y=avgMPG, color='black', linestyle=':')

# show plot
plt.show()


# Color the points in the plot according to whether the transmission
# is manual or automatic. <br> Use blue if automatic (am = 0) and orange if manual (am = 1).<br>
# 
# Note: blue/orange are easy to distinguish for many people, even most
# people with some form of colorblindness.)

# In[47]:


# https://stackoverflow.com/questions/43482446/python-scatter-plot-different-colors-depending-on-value

# Change automatic dot to blue (am = 0).
# Change manual dot to orange (am = 1).
colors = np.where(df['am']==1, 'orange', 'blue')

# Create scatter plot
plt.scatter(df['disp'],df['mpg'], color=colors)


# Add a legend.<br>
# 
# You may want to do this by splitting the data up, and then<br>
# calling plt.scatter() twice, once for am=0 and once for am=1.<br>
# 
# Hint: use the 'label' parameter in plt.scatter(), and then plt.legend().

# In[78]:


# https://stackoverflow.com/questions/71326966/plot-graph-for-only-one-specific-value-in-a-column

# Change automatic dot to blue (am = 0).
# Change manual dot to orange (am = 1).
colors = np.where(df2['am']==1, 'orange', 'blue')
colors2 = np.where(df3['am']==1, 'orange', 'blue')

# Create scatter plot for am=0
df2 = df.loc[(df['am']==0)] # datafram where 'am=0'

# Plot this graph
plt.scatter(df2['disp'],df2['mpg'], color=colors, label="automatic")

# Create scatter plot for am=1
df3 = df.loc[(df['am']==1)]

# Plot this graph 
plt.scatter(df3['disp'], df3['mpg'], color=colors2, label="manual")

# Add title 
plt.title('Car MPG as a Function of Engine Displacement')

# Add labels
plt.xlabel('miles per gallon')
plt.ylabel('cu. inches')

# Compute the average mpg
avgMPG = df['mpg'].mean()
print(f"avgMPG = {avgMPG}")

# Plot horizontal dotted line
plt.axhline(y=avgMPG, color='black', linestyle=':', label="avg mpg")

# Show lengend
plt.legend()

# Show plot
plt.show()


# Compute the number of cars for each possible value of number of cylinders, <br>
# and assign the result to variable 'cyl_counts'.<br>
# 
# Hint: you can use this code:  cyl_counts = df['cyl'].value_counts()

# In[91]:


cyl_counts = df['cyl'].value_counts()


# Using matplotlib, make a bar plot showing the number
# of cars for each number of cylinders.

# In[90]:


# x = # of cylinders
# y = # of cars
plt.bar(df['cyl'].unique(), cyl_counts)


# Improve your plot by adding title, x and y axis labels, and the color
# of your choice.

# In[97]:


# x = # of cylinders
# y = # of cars
plt.bar(df['cyl'].unique(), cyl_counts)

# Add title, x,y,lable, color
plt.title('Number of Cars with Different Numbers of Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Number of Cars')

# Show plot
plt.show()


# Repeat the process, but this time use Seaborn to create your
# barplot. <br>
# 
# Note: you can use plt.title() to give your plot a title.

# In[ ]:





# Create a histogram of mpg values, using matplotlib, then<br>
# seaborn, then pandas

# In[ ]:





# If you still have time, experiment with seaborn and pandas plots.<br>
# For example, in pandas, what happens if you try to plot two columns<br>
# of the mtcars data?

# In[ ]:





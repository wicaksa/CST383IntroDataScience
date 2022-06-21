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


#@ 1. We’ll explore the 1994 US census summary data that is available here:


# In[3]:


#@ 2. Create a Python file in Spyder, and write code to load the data.


# In[4]:


link = "https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv"
df = pd.read_csv(link)


# In[5]:


#@ 3. Visually explore the data frame using the Variable explorer tab in Spyder, which can be found in the upper right panel.
display(df)


# In[6]:


#@ 4.Which Pandas commands can you use to get a quick overview of the data?
#### You can use df.info(), df.head(), or display(df)


# In[7]:


#@ 5. Remove the 'usid' and 'fnlwgt' columns from the data frame.


# In[8]:


df.drop(['usid', 'fnlwgt'], axis=1)


# In[9]:


#@ 6. Use a Pandas command to look at the first rows of the data frame.
df.head(1)


# In[10]:


#@ 7. The ‘education_num’ column records the number of years of education.  
#### Use ‘describe’ to find min, max, median values for education_num.  
#### Plot education_num using a histogram.  Label the x axis with 'years of education'.

df['education_num'].min() # 1
df['education_num'].max() # 16
df['education_num'].median() # 10.0

ed_num_hist = df['education_num'].plot.hist(title="Years of Education of People")
ed_num_hist.set_xlabel("Years of Education")


# In[11]:


#@ 8. Does it make sense to use education_num with a histogram?  
####Try it, and compare with a plot using a bar plot of the count of the rows by education_num (as shown in lecture).
x = df['education_num'].value_counts().to_numpy()
df['education_num'].value_counts()


# In[12]:


#@ 9. Plot capital_gain with a density plot.  
#### Did you find anything interesting?  Save your plot to a png file.


# In[13]:


df.capital_gain.plot.density(color='green')
plt.title('Density Plot For Capital Gain')
plt.show()


# In[14]:


#@ 10. Investigate attribute ‘workclass’.  Plot it in an appropriate way.


# In[15]:


df['workclass'].value_counts()


# In[16]:


#x = (np.unique(df['workclass'].tolist())).tolist()
x = ['Private', 'Self_emp_not_inc', 'Local_gov', 'State_gov', 'Self_emp_inc', 'Federal_gov', 'Without_pay','Never_worked']
y = df['workclass'].value_counts().to_numpy()


# In[17]:


plt.bar(x,y, width=.4)
plt.xlabel("Types of Work")
plt.ylabel("Frequency")
plt.title("Work Class")
plt.show()


# In[18]:


#@ 11. Use a bar plot to show the distribution of attribute ‘sex’.  
#### Label the 'Male' and 'Female' bars with the fraction of rows associated with each sex (not a count).  
#### Comment on what you find.  Why do you think the distribution is like this?
#### There are twice as many men than women. 


# In[19]:


x = (np.unique(df['sex'].tolist())).tolist()
y = df['sex'].value_counts()
plt.bar(x,y, width=.4)
plt.xlabel("Gender")
plt.ylabel("Number of Genders")
plt.title("Distribution of Genders")
plt.show()


# In[20]:


#@ 12. Use a horizontal bar plot to visualize attribute marital_status.
x = (np.unique(df['marital_status'].tolist())).tolist()
y = df['marital_status'].value_counts()

plt.barh(x, y)
plt.show()


# In[21]:


#@ 13. If you have time, visualize all the attributes you haven’t explored yet.  Be sure to include 'native_country'


# In[22]:


#@ 14. If you still have time, do single-variable visualization for the attributes in the contribution campaign data.


# In[ ]:





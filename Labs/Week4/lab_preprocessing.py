# Wicaksa Munajat
# CST 383 Summer 2022
# 05/20/2022

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
pd.set_option('display.max_columns', 500)


# In[2]:


#@1. Read the red wine data, which measures physical characteristics of wine, and whether people like the taste of the wine.  
#### Note the use of the ‘sep’ parameter in read_csv().


# In[3]:


wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")


# In[4]:


#@2. Make a small version of the data set named 'df' by selecting 20 random rows of it.  
#### Use the small version until instructed otherwise.


# In[5]:


df = wine.sample(n=20)


# In[6]:


#@3. Scale the data using Z score normalization.


# In[7]:


normalized_df=(df-df.mean())/df.std()
normalized_df


# In[8]:


#@4. In the scaled data, find the column minimums (a vector containing the minimum value for each column).


# In[9]:


normalized_df.describe().loc['min']
"""
fixed acidity          -2.199813
volatile acidity       -1.803453
citric acid            -1.718811
residual sugar         -0.600415
chlorides              -1.101506
free sulfur dioxide    -0.998811
total sulfur dioxide   -0.999058
density                -2.287214
pH                     -2.672299
sulphates              -1.122590
alcohol                -1.088392
quality                -2.012461
Name: min, dtype: float64
"""


# In[10]:


#@5. Repeat, but for the column maximums.  Did you get the kinds of values you expected?


# In[11]:


normalized_df.describe().loc['max']
"""
fixed acidity           1.568954
volatile acidity        1.774129
citric acid             1.936869
residual sugar          3.549918
chlorides               3.844545
free sulfur dioxide     2.996433
total sulfur dioxide    2.331134
density                 1.946535
pH                      1.872960
sulphates               3.352852
alcohol                 2.574466
quality                 2.459675
Name: max, dtype: float64
"""


# In[12]:


#@6. Scale the data again using unit-interval normalization.  
#### Scale the original small data set, not the version you just normalized.


# In[ ]:





# In[13]:


#@7. Again, find the column mins and maxes.  Did you get what you expected?


# In[ ]:





# In[14]:


#@8. Now we’ll return to the full data set.  
#### Use 'df = wine' to assign 'wine' to variable 'df', then compute the correlation coefficient.
#### Use function pandas.dataframe.corr(r) to see how the features are correlated.


# In[15]:


df = wine
df.corr()


# In[16]:


#@9. Looking at the matrix of correlations, which features are the most positively correlated?  (Don't consider the correlation between a feature and itself.)  
#### Which are the most negatively correlated?


# In[17]:


def most_corr_index(x):
return x.sort_values(ascending=False).index[1]
df.corr().apply(most_corr_index)
"""
fixed acidity                    citric acid
volatile acidity                          pH
citric acid                    fixed acidity
residual sugar                       density
chlorides                          sulphates
free sulfur dioxide     total sulfur dioxide
total sulfur dioxide     free sulfur dioxide
density                        fixed acidity
pH                          volatile acidity
sulphates                          chlorides
alcohol                              quality
quality                              alcohol
dtype: object

"""


# In[18]:


#@10. Display the correlations with a plot, and answer the questions of the previous problem again.


# In[19]:


corr = df.corr()


# In[20]:


sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)


# In[21]:


#@11. Which features are most correlated to the ‘quality’ variable?  
#### Express what you find in plain English?
#### This is mostly correlated with alcohol it looks like with a 0.5 correlation.
#### There is a strong relationship between quality and alcohol content. 


# In[22]:


#@12. Is the wine data tidy? 
#### Yes


# In[23]:


#@13. Generate some fake GPA data using the following code:
n=10   # number of students
sem_years = np.array([s+' '+str(y) for y in np.arange(14,19) for s in ['spring', 'fall']])
gpa = np.random.normal(loc=3, scale=0.5, size=(n,sem_years.size))
gpa = np.clip(gpa, 0, 4)
gpa = pd.DataFrame(gpa, columns=sem_years)
otter_ids = pd.DataFrame({'otter_id': np.random.randint(1000, 10000, n)})
gpa_by_semester = pd.concat([otter_ids, gpa], axis=1)


# In[24]:


#@14. Convert the data into the long format.  
#### Change the column names appropriately.
otter_ids.head()
gpa_by_semester.head()
gpa_long = pd.melt(gpa_by_semester, id_vars=['otter_id'])


# In[25]:


#@15. If you still have time, sort the data frame by otter ID, then by semester (with ‘spring18’ before ‘fall18’ before ‘spring19’, etc.).  This is not a trivial problem.

